from .filters import UserProfileFilter
from .forms import ExerciseForm, SignUpForm, UploadImageForm
from .models import Machine, UserProfile, Exercise, UserImages, Relationship

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
# from django.core.files import File
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import View

from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg
# from PIL import ExifTags
# from PIL import Image as Img

# from reportlab.lib import colors
# from reportlab.lib.units import cm
# from reportlab.pdfgen import canvas
# from reportlab.platypus import Table, TableStyle

import io
import matplotlib.pyplot as plt


# Create your views here.


@login_required
def index(request):
    """
    View of the main page
    """
    actual_user = ''
    requests = ''
    friends = ''
    friends_list = []
    try:
        if not request.user.is_anonymous:
            actual_user = UserProfile.objects.get(
                pk=request.user.userprofile.pk)
            requests = get_only_requests(
                actual_user, 1)
            if requests:
                messages.error(
                    request, 'Tienes una nueva petición de amistad')
            friends = actual_user.followers.filter(
                to_people__status=settings.RELATIONSHIP_FOLLOWING,
                to_people__from_person=actual_user,
                from_people__status=settings.RELATIONSHIP_BLOCKED,
                from_people__to_person=actual_user)
        for x in requests:
            friends_list.append(x)
        for x in friends_list:
            if x in friends:
                friends_list.remove(x)
    except UserProfile.DoesNotExist:
        actual_user = ''
        requests = ''
        friends = ''

    return render(request, 'index.html', {
        'requests': requests, 'friends': friends})


def machines(request):
    """
    View of the page of the available machines
    """
    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'gym/maquinas.html', context)


class UserListView(generic.ListView):
    """
    Generic view of the users list
    """
    model = UserProfile
    context_object_name = 'users_list'
    template_name = 'gym/users_list.html'


def user_data(request):
    """
    View of user's details
    """
    weight = ''
    try:
        user_data = UserProfile.objects.get(user_id=request.user.id)
    except UserProfile.DoesNotExist:
        user_data = ''
    if user_data:
        try:
            last_image = user_data.user_images.last()
            weight = last_image.weight
        except:
            weight = ''

    context = {'user_data': user_data, 'weight': weight}

    return render(request, 'gym/datos_usuario.html', context)


class MachineDetailView(generic.DetailView):
    """
    Generic view of the machine's details
    """
    model = Machine
    template_name = 'gym/maquina_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MachineDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', None)
        if not self.request.user.is_anonymous:
            try:
                weights = Exercise.objects.filter(
                    machine__pk=pk).filter(
                    user_id=self.request.user.userprofile.id).order_by('-date')
            except Exercise.DoesNotExist:
                weights = ''
            context['query'] = weights
            context['query2'] = weights.count() + 1
            context['pk'] = pk
        else:
            context['query'] = ''

        return context


def new_weight(request, pk=None):
    """
    View for create a new weight used in one machine
    """
    maquina = None
    if request.method == "POST":
        form = ExerciseForm(request.POST, request=request)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = UserProfile.objects.get(user=request.user)
            machine_id = form.cleaned_data.get('machine').id
            try:
                profile.save()
                messages.success(
                    request, 'Ejercicio añadido correctamente')
            except Exception as e:
                messages.error(request, 'Ocurrió un error al añadir el ejercicio')
            return HttpResponseRedirect(reverse(
                'machine-detail', args=[machine_id]))
    else:
        if not request.user.is_anonymous:
            user_exercise = UserProfile.objects.get(user=request.user)
            if pk:
                maquina = Machine.objects.get(id=pk)
            form = ExerciseForm(
                request=request, instance=user_exercise, maquina=maquina)
        else:
            form = ExerciseForm()
    return render(request, 'gym/post_peso_ejercicio.html', {'form': form})


def signup(request):
    """
    View for signup in the application
    """
    lista = []
    for x in range(len(settings.PROVINCIAS)):
        lista.append(x)
    cities = dict(zip(lista, settings.PROVINCIAS))

    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES, cities=cities.items())
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.birthdate = form.cleaned_data.get('birthdate')
            user.userprofile.user.first_name = form.cleaned_data.get(
                'first_name')
            user.userprofile.user.email = form.cleaned_data.get('email')
            user.userprofile.user.last_name = form.cleaned_data.get(
                'last_name')
            citi = cities.get(int(form.cleaned_data.get('city')))
            user.userprofile.profile_picture = form.cleaned_data.get(
                'profile_picture')
            user.userprofile.city = citi
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            return redirect('index')
    else:
        form = SignUpForm(cities=cities.items())
    return render(request, 'signup.html', {'form': form, 'mobile': mobile})


class UsersReportPDF(View):
    pass
    # """
    # Class to create pdf with the list of users
    # """

    # def get(self, request, *args, **kwargs):
    #     response = HttpResponse(content_type='application/pdf')
    #     buffer = BytesIO()
    #     pdf = canvas.Canvas(buffer)
    #     self.header(pdf)
    #     y = 600
    #     self.users_table(pdf, y)
    #     pdf.save()
    #     pdf = buffer.getvalue()
    #     buffer.close()
    #     response.write(pdf)
    #     return response

    # def header(self, pdf):
    #     """
    #     Header of the PDF
    #     """
    #     # logo =  'static/logo-gym.png'
    #     # pdf.drawImage(logo, 40, 700, 100, 100)
    #     pdf.setFont("Helvetica", 16)
    #     pdf.drawString(250, 750, u"Lista de usuarios")

    # def users_table(self, pdf, y):
    #     """
    #     Table for the user list
    #     """
    #     titles = ('Nombre', 'Apellidos', 'Fecha de nacimiento')
    #     items = [(
    #         person.user.first_name,
    #         person.user.last_name,
    #         person.birthdate) for person in
    #         UserProfile.objects.all() if not
    #         person.user.is_staff]
    #     all_items = Table([titles] + items, colWidths=[5 * cm])
    #     all_items.setStyle(
    #         TableStyle([
    #             ('ALIGN', (0, 0), (2, 0), 'CENTER'),
    #             ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #             ('FONTSIZE', (0, 0), (2, 0), 10),
    #             ('BACKGROUND', (0, 0), (2, 0), colors.grey),
    #         ]
    #         ))
    #     all_items.wrapOn(pdf, 800, 600)
    #     all_items.drawOn(pdf, 60, y)


class ExerciseUpdate(SuccessMessageMixin, generic.UpdateView):
    model = Exercise
    fields = ['name', 'machine', 'weight', 'date']
    template_name_suffix = '_update_form'
    success_message = 'Ejercicio actualizado correctamente'

    def get_success_url(self):
        return reverse('machine-detail', args=[int(self.kwargs.get('id'))])


class ExerciseDelete(SuccessMessageMixin, generic.DeleteView):
    """
    Generic view for delete a exercise
    """
    model = Exercise
    context_object_name = 'exercise'
    fields = ['name', 'machine', 'weight', 'date']
    success_message = "Ejercicio eliminado correctamente"

    def get_context_data(self, **kwargs):
        context = super(ExerciseDelete, self).get_context_data(**kwargs)
        context['machine'] = Machine.objects.get(pk=int(self.kwargs.get('id')))
        return context

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(ExerciseDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('machine-detail', args=[int(self.kwargs.get('id'))])


def edit_userprofile(request):
    """
    View for edit an user
    """
    lista = []
    for x in range(len(settings.PROVINCIAS)):
        lista.append(x)
    cities = dict(zip(lista, settings.PROVINCIAS))

    if request.method == 'POST':
        form = SignUpForm(
            request.POST,
            request.FILES, instance=request.user, cities=cities.items())
        if form.is_valid():
            user = form.save(commit=False)
            user.userprofile.birthdate = form.cleaned_data.get('birthdate')
            user.userprofile.user.first_name = form.cleaned_data.get(
                'first_name')
            user.userprofile.user.last_name = form.cleaned_data.get(
                'last_name')
            city = cities.get(int(form.cleaned_data.get('city')))
            user.userprofile.profile_picture = form.cleaned_data.get(
                'profile_picture')
            user.userprofile.city = city
            try:
                user.save()
                messages.success(
                    request, 'Usuario actualizado correctamente')
            except Exception as e:
                messages.error(
                    request, 'Ocurrió un error al actualizar el usuario')
            return redirect('logout')
    else:
        form = SignUpForm(instance=request.user, cities=cities.items())
    return render(request, 'gym/userprofile_update_form.html', {'form': form})


def plot(request, pk):
    """
    Set each graph to be shown in the progress view
    """
    if pk == '0':
        images = UserImages.objects.filter(
            user__pk=request.user.userprofile.pk)
        x, y = [], []
        for weight in images:
            y.append(int(weight.weight))
            x.append(weight.date.day)
    else:
        weights = Exercise.objects.filter(
            user__pk=request.user.userprofile.pk,
            machine_id=pk).order_by('date')
        x, y = [], []
        for weight in weights:
            y.append(int(weight.weight))
            x.append(weight.date.month)

    f = plt.figure()

    axes = f.add_axes([0.15, 0.15, 0.75, 0.75])
    axes.plot(x, y, 'o-')
    axes.set_xlabel("Fecha")
    axes.set_ylabel("Peso")

    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    response = HttpResponse(buf.getvalue(), content_type='image/png')

    f.clear()

    response['Content-Length'] = str(len(response.content))

    return response


def progress(request):
    """
    Shows progress graphs
    """
    machines = Machine.objects.all()
    count = machines.count() + 1
    return render(request, 'gym/progress.html', {
        'range': range(1, count), 'machines': machines})


def upload_image(request):
    """
    View to upload a new image
    """
    # import cv2

    # cv2.namedWindow("webcam")
    # vc = cv2.VideoCapture(0)

    # while True:
    #     next, frame = vc.read()
    #     cv2.imshow("webcam", frame)
    #     if cv2.waitKey(50) >= 0:
    #         break

    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            # if mobile(request):
            #     imagen = form.cleaned_data.get('image')
            #     pilImage = Img.open(BytesIO(imagen.read()))
            #     for orientation in ExifTags.TAGS.keys():
            #         if ExifTags.TAGS[orientation] == 'Orientation':
            #             break
            #     try:
            #         exif = dict(pilImage._getexif().items())
            #         if exif[orientation] == 3:
            #             pilImage = pilImage.rotate(180, expand=True)
            #         elif exif[orientation] == 6:
            #             pilImage = pilImage.rotate(270, expand=True)
            #         elif exif[orientation] == 8:
            #             pilImage = pilImage.rotate(90, expand=True)
            #         output = BytesIO()
            #         pilImage.save(output, format='JPEG', quality=75)
            #         output.seek(0)
            #         imagen = File(output, imagen.name)
            #         profile.image = imagen
            #     except KeyError:
            #         pass
            profile.user = UserProfile.objects.get(user=request.user)
            try:
                profile.save()
                messages.success(
                    request, 'Imagen subida correctamente')
            except Exception as e:
                messages.error(
                    request, 'Ocurrió un error al subir la imagen')
            return HttpResponseRedirect('/gym/images/')
    else:
        user_image = UserProfile.objects.get(user=request.user)
        form = UploadImageForm(instance=user_image)

    return render(request, 'gym/upload.html', {
        'form': form})


def images_view(request, pk=None):
    """
    View to show the user's images and his/her measures
    """
    actual_user = UserProfile.objects.get(pk=request.user.userprofile.pk)
    friends = get_friends(actual_user)
    flag = ''
    actual = True
    if friends and pk:
        for x in friends:
            if int(pk) == x.pk:
                flag = 1
    if flag:
        images = UserImages.objects.filter(user_id=pk)
        usuario = UserProfile.objects.get(pk=pk)
        usuario = 'de ' + str(usuario)
    else:
        images = UserImages.objects.filter(user__user=request.user)
        usuario = UserProfile.objects.get(
            pk=request.user.userprofile.pk)
        usuario = 'de ' + str(usuario)
    try:
        user_image = UserImages.objects.filter(user_id=pk)[0].user
        if user_image and actual_user != user_image:
            actual = False
    except:
        actual = True

    return render(request, 'gym/images.html', {
        'images': images, 'pk': pk, 'usuario': usuario, 'actual': actual})


class UserImagesUpdate(SuccessMessageMixin, generic.UpdateView):
    """
    Generic view to update an userprofile image
    """
    model = UserImages
    fields = [
        'image', 'date', 'weight', 'chest', 'biceps', 'waist',
        'quadricep', 'gastrocnemius', 'muscle_mass', 'muscle_fat']
    template_name_suffix = '_update_form'
    success_message = 'Datos actualizados correctamente'

    def get_success_url(self):
        return reverse('images')


class ImageDelete(generic.DeleteView):
    """
    Generic view to delete a image
    """
    model = UserImages
    context_object_name = 'image'
    success_message = 'Imagen eliminada correctamente'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(ImageDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('images')


def users_search(request):
    """
    View to search an user registered in the platform
    """
    users = UserProfile.objects.all().exclude(pk=request.user.userprofile.pk)
    actual_user = UserProfile.objects.get(pk=request.user.userprofile.pk)
    relationships = get_relationships(actual_user, 1)
    filter = UserProfileFilter(request.GET, queryset=users)
    return render(request, 'gym/users_search.html', {
        'filter': filter, 'actual_user': actual_user,
        'relationships': relationships})


def mobile(request):
    """
    Return True if the request comes from a mobile device
    """
    import re

    MOBILE_AGENT_RE = re.compile(
        r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False


def social(request):
    """
    View to the index of the social section
    """
    return render(request, 'gym/index_social.html')


def add_relationship(request, pk, add_friend=None):
    """
    View to add relationship with another user of the platform
    """
    actual_user = UserProfile.objects.get(pk=request.user.userprofile.pk)
    add_user = UserProfile.objects.get(pk=pk)
    try:
        relationship = Relationship.objects.get(
            from_person=add_user,
            to_person=actual_user)
        relationship.accepted = True
        relationship.status = settings.RELATIONSHIP_FOLLOWING
        try:
            relationship.save()
            messages.success(
                request, 'Petición aceptada correctamente')
        except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar la petición')
        relationship, created = Relationship.objects.get_or_create(
            from_person=actual_user,
            to_person=add_user,
            status=1)
        relationship.accepted = True
        relationship.status = settings.RELATIONSHIP_FOLLOWING
    except Relationship.DoesNotExist:
        relationship, created = Relationship.objects.get_or_create(
            from_person=actual_user,
            to_person=add_user,
            status=1)
        try:
            relationship.save()
            messages.success(
                request, 'Petición enviada correctamente')
        except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar la petición')
    if add_friend == '0':
        return HttpResponseRedirect(reverse('requests'))
    return HttpResponseRedirect(reverse('users_search'))


def delete_relationship(request, pk, delete_friend=None):
    """
    View to delete a relatioship created between two users
    """
    actual_user = UserProfile.objects.get(pk=request.user.userprofile.pk)
    delete_user = UserProfile.objects.get(pk=pk)
    try:
        Relationship.objects.filter(
            from_person=actual_user,
            to_person=delete_user).delete()
        Relationship.objects.filter(
            from_person=delete_user,
            to_person=actual_user).delete()
        messages.error(
            request, 'Contacto eliminado correctamente')
    except Exception as e:
        messages.error(request, 'Ocurrió un error al eliminar el contacto')
    if delete_friend == '0':
        return HttpResponseRedirect(reverse('view_friends'))
    elif delete_friend == '2':
        return HttpResponseRedirect(reverse('requests'))
    return HttpResponseRedirect(reverse('users_search'))


def delete_relationship_confirm(request, pk, delete_friend=None):
    """
    View to confirm the elimination of a relationship
    """
    return render(request, 'gym/relationship_confirm_delete.html', {
        'pk': pk, 'delete_friend': delete_friend})


def get_relationships(self, status):
    """
    Function that returns users to whom we have sent a friend request
    """
    return self.followers.filter(
        to_people__status=status,
        to_people__from_person=self)


def get_related_to(self, status):
    """
    Function that returns users whom have any relationship
    """
    return self.related_to.filter(
        from_people__status=status,
        from_people__to_person=self)


def get_friends(self):
    """
    Function that returns all ours friends
    """
    return self.followers.filter(
        to_people__status=settings.RELATIONSHIP_FOLLOWING,
        to_people__from_person=self,
        from_people__status=settings.RELATIONSHIP_FOLLOWING,
        from_people__to_person=self)


def get_only_requests(self, status):
    """
    Function that returns the users who sent us a friend request
    """
    return self.related_to.filter(
        from_people__status=status,
        from_people__to_person=self,
        from_people__accepted=False)


def view_friends(request):
    """
    View to show our friends images and measures
    """
    actual_user = UserProfile.objects.filter(id=request.user.userprofile.pk)[0]
    user_friends = get_friends(actual_user)
    filter = UserProfileFilter(request.GET, queryset=user_friends)
    return render(request, 'gym/users_search.html', {
        'filter': filter, 'user_friends': user_friends})


def view_requests(request):
    """
    View to show the users who sent us a friend request
    """
    actual_user = UserProfile.objects.get(pk=request.user.userprofile.pk)
    requests = get_only_requests(actual_user, 1)
    filter = UserProfileFilter(request.GET, queryset=requests)
    return render(request, 'gym/view_requests.html', {
        'filter': filter})
