import bisect, logging, json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .forms import TuggerForm, TypyForm, RacksForm, AGVForm, VNAForm
from pages.models import Klienci, Oddzialy, RealizacjeAGV, RealizacjeRacks, RealizacjeTugger, RealizacjeVNA, Telefony, Tugger

logger = logging.getLogger(__name__)


class AuthMixin(object):
    @method_decorator(login_required(login_url='/accounts/login/'))
    def dispatch(self, *args, **kwargs):
        return super(AuthMixin, self).dispatch(*args, **kwargs)


class HomePageView(AuthMixin, TemplateView):
    template_name = 'home.html'


class KlienciPageView(AuthMixin, TemplateView):
    template_name = 'klienci.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # k = Klienci.objects.all().exclude(Vxx__isnull=True).filter(Vxx="12")
        k = Klienci.objects.all().exclude(Vxx__isnull=True)
        context['Klienci'] = k
        return context


class TelefonyPageView(AuthMixin, TemplateView):
    template_name = 'telefony.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # app = xw.App()
        zbior = xw.books.open(r'C:\Users\pl6156\Listy\Książka telefoniczna\Książka_telefoniczna 2020.04.xlsx').sheets[
            'TABELA'].range('A10:H494').options(numbers=int).value
        dzial = None
        poddzial = None
        # for i in range (1, len(zbior)):
        # for i in range (1, 1):
        #    zbior[i] = zbior[1,1]
        for i in range(0, len(zbior)):
            dzial = [zbior[i][0], dzial][zbior[i][0] is None]
            # print(dzial)
            poddzial = [zbior[i][1], poddzial][zbior[i][1] is None]
            # print(poddzial)
            if zbior[i][4] is not None:
                created = Telefony.objects.update_or_create(imie=[zbior[i][4].split(" ")[1], ""][zbior[i][4] is None],
                                                            nazwisko=[zbior[i][4].split(" ")[0], ""][
                                                                zbior[i][4] is None],
                                                            stacjonarny=[zbior[i][6], ""][zbior[i][6] is None],
                                                            komorkowy=[zbior[i][7], ""][zbior[i][7] is None],
                                                            dzial=dzial, poddzial=poddzial,
                                                            stanowisko=[zbior[i][2], ""][zbior[i][2] is None],
                                                            oddzial=[zbior[i][3], ""][zbior[i][3] is None])

        # xw.books[0].close()
        # context['Telefony'][i] =

        # FLOW = OAuth2WebServerFlow(
        #    client_id='948358153713-8usrh66n5apo6ffp1a4lg5n6ge2j58n3.apps.googleusercontent.com',
        #    client_secret='SgY50jyLl1_RblucgIfHIC1n',
        #    scope='https://www.googleapis.com/auth/contacts.readonly',
        #    user_agent='dominikjasiok-262519/Klient sieci Web 1')

        # If the Credentials don't exist or are invalid, run through the
        # installed application flow. The Storage object will ensure that,
        # if successful, the good Credentials will get written back to a
        # file.
        # storage = Storage(r'C:\Users\pl6156\WEB\still\pages\info.dat')
        # credentials = storage.get()
        # if credentials is None or credentials.invalid == True:
        #    credentials = run_flow(FLOW, storage)

        # Create an httplib2.Http object to handle our HTTP requests and
        # authorize it with our good Credentials.
        # http = httplib2.Http()
        # http = credentials.authorize(http)

        # Build a service object for interacting with the API. To get an API key for
        # your application, visit the Google API Console
        # and look at your application's credentials page.
        # people_service = build(serviceName='people', version='v1', http=http)

        context['Tele'] = 'OK'
        return context


class KontaktPageView(AuthMixin, TemplateView):
    template_name = 'kontakt.html'


class MapaPageView(AuthMixin, TemplateView):
    template_name = 'mapa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # logger.warning(context)

        # ctx = ClientContext("https://kion-my.sharepoint.com/").with_user_credentials("dominik.jasiok@still.pl", "QETUO0p;/")

        #tenant_url = "https://kion-my.sharepoint.com"
        #ctx_auth = AuthenticationContext(tenant_url)

        #site_url = "https://kion-my.sharepoint.com/sites/KION_STILL_PL_AA_KMA2"

        #if ctx_auth.acquire_token_for_user("dominik.jasiok@still.pl", "QETUO0p;/"):
        #    request = ClientRequest(ctx_auth)
        #    options = RequestOptions("{0}/_api/web/".format(site_url))
        #    options.set_header('Accept', 'application/json')
        #    options.set_header('Content-Type', 'application/json')
        #    data = request.execute_request_direct(options)
        #    s = json.loads(data.content)
        #    web_title = s['Title']
        #    logger.warning("Web title: " + web_title)
        #else:
        #    logger.warning(ctx_auth.get_last_error())

        # logger.warning(web.properties["Url"])

        context['form'] = TypyForm()
        #context['Klienci'] = Klienci.objects.all().exclude(Vxx__isnull=True)
        return context

    # def get(self, request, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Klienci'] = Klienci.objects.all().exclude(Vxx__isnull=True)
    #     logger.warning("JEST")

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if (request.POST.get('choose') == ''):
            context['form'] = TypyForm(request.POST)
            # context['Klienci'] = Klienci.objects.all()
            # k = Klienci.objects.all().exclude(Vxx__isnull=True).filter(Vxx="12")
            # k = Klienci.objects.all().exclude(Vxx__isnull=True)
            context['Klienci'] = Klienci.objects.all().exclude(Vxx__isnull=True)

        if (request.POST.get('choose') == 'T'):
            context['form'] = TuggerForm(request.POST)
            context['Klienci'] = Klienci.objects.all() \
                .filter(SAP__in=RealizacjeTugger.objects \
                        .filter(typ__in=list(map(str, RealizacjeTugger.TYP)) if request.POST.get(
                'typ') == None else request.POST.getlist('typ')) \
                        .filter(podnoszenie__in=list(map(str, RealizacjeTugger.PODNOSZENIE)) if request.POST.get(
                'podnoszenie') == None else request.POST.getlist('podnoszenie')) \
                        .filter(wymiar__in=list(map(str, RealizacjeTugger.WYMIAR)) if request.POST.get(
                'wymiar') == None else request.POST.getlist('wymiar')) \
                        .order_by('klient').values('klient_id').distinct())

        if (request.POST.get('choose') == 'R'):
            context['form'] = RacksForm(request.POST)
            context['Klienci'] = Klienci.objects.all() \
                .filter(SAP__in=RealizacjeRacks.objects \
                        .filter(typ__in=list(map(str, RealizacjeRacks.TYP)) if request.POST.get(
                'typ') == None else request.POST.getlist('typ')) \
                        .filter(ilosc__in=list(map(str, RealizacjeRacks.ILOSC)) if request.POST.get(
                'ilosc') == None else request.POST.getlist('ilosc')) \
                        .filter(wysokosc__in=list(map(str, RealizacjeRacks.WYSOKOSC)) if request.POST.get(
                'wysokosc') == None else request.POST.getlist('wysokosc')) \
                        .filter(korytarz__in=list(map(str, RealizacjeRacks.KORYTARZ)) if request.POST.get(
                'korytarz') == None else request.POST.getlist('korytarz')) \
                        .order_by('klient').values('klient_id').distinct())

        if (request.POST.get('choose') == 'S'):
            context['form'] = VNAForm(request.POST)
            context['Klienci'] = Klienci.objects.all() \
                .filter(SAP__in=RealizacjeVNA.objects \
                        .filter(
                typ__in=list(map(str, RealizacjeVNA.TYP)) if request.POST.get('typ') == None else request.POST.getlist(
                    'typ')) \
                        .filter(wysokosc__in=list(map(str, RealizacjeVNA.WYSOKOSC)) if request.POST.get(
                'wysokosc') == None else request.POST.getlist('wysokosc')) \
                        .filter(prowadzenie__in=list(map(str, RealizacjeVNA.PROWADZENIE)) if request.POST.get(
                'prowadzenie') == None else request.POST.getlist('prowadzenie')) \
                        .filter(hamowanie__in=list(map(str, RealizacjeVNA.HAMOWANIE)) if request.POST.get(
                'hamowanie') == None else request.POST.getlist('hamowanie')) \
                        .filter(trog__in=list(map(str, RealizacjeVNA.TROG)) if request.POST.get(
                'trog') == None else request.POST.getlist('trog')) \
                        .filter(typbaterii__in=list(map(str, RealizacjeVNA.TYPBATERII)) if request.POST.get(
                'typbaterii') == None else request.POST.getlist('typbaterii')) \
                        # .filter(hamowanie__in=list(map(str, RealizacjeVNA.HAMOWANIE)) if request.POST.get('hamowanie')==None else request.POST.getlist('hamowanie')) \
                        .order_by('klient').values('klient_id').distinct())

        if (request.POST.get('choose') == 'A'):
            context['form'] = AGVForm(request.POST)
            context['Klienci'] = Klienci.objects.all() \
                .filter(SAP__in=RealizacjeAGV.objects \
                        .filter(
                typ__in=list(map(str, RealizacjeAGV.TYP)) if request.POST.get('typ') == None else request.POST.getlist(
                    'typ')) \
                        .filter(truck__in=list(map(str, RealizacjeAGV.TRUCK)) if request.POST.get(
                'truck') == None else request.POST.getlist('truck')) \
                        .order_by('klient').values('klient_id').distinct())

            # logger.warning(context['Klienci'].query)
        #
        # if not (request.POST.get('choose') == ''):
        #     gmaps = googlemaps.Client(key='AIzaSyByyU8uYPlEpanMFDLhhFgespHrLc4w8SQ')
        #     # logger.warning("DUPA")
        #     for klient in context['Klienci']:
        #         if (klient.lat is None) | (klient.long is None):
        #             geocode_result = gmaps.geocode(
        #                 address=klient.Nazwa + ', ' + klient.Ulica + ' ' + klient.Numer + ', ' + klient.Miejscowosc,
        #                 components={"postal_code": klient.Kodpocztowy},
        #                 region='PL',
        #                 language='PL')
        #             logger.warning("SZUKA")
        #             if geocode_result:
        #                 klient.lat = geocode_result[0]["geometry"]["location"]["lat"]
        #                 klient.long = geocode_result[0]["geometry"]["location"]["lng"]
        #                 klient.save()
        #                 logger.warning("ZAPISUJE")
        #             else:
        #                 klient.lat = 0
        #                 klient.long = 0
        #                 klient.save()
        #                 logger.warning("NIE ZAPISUJE")
        #         if klient.Vxx is None:
        #             klient.Vxx = wyszukajkod(klient.Kodpocztowy)
        #             klient.save()
        #             logger.warning("ZAPISUJE HANDLOWCA")

        # logger.warning(request.POST)

        return render(request, self.template_name, context)


def load_infowindow(request):
    if request.method == 'POST':
        # request_data = request.POST.get('SAP', '')
        # request_data = request.data['SAP']
        request_data = request.POST['SAP']
        k = Klienci.objects.filter(SAP=request_data).get()
        ###t = RealizacjeTugger.objects.filter(klient_id=request_data).all()
        #objects.all().filter(SAP=request_data).order_by('Data')
        # request_data = "SAP"
        # do something

        response_data = {}
        response_data['infowindow'] = "<b>" + request_data + "</b>, </br>" + k.Nazwa + "</br><b>V" + k.Vxx + "</b></br>"
        ###for tug in t:
        ###    response_data['infowindow'] += "<b>S/N: " + tug.numer_seryjny + "</b> " + tug.typ + " / " + tug.podnoszenie + " / " + tug.wymiar + "</br>"
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def load_data(request):
    if request.method == 'POST':
        response_data = {}
        if request.POST['typ'] == "TT":
            response_data = Klienci.objects.all().filter(Vxx=request.POST['Vxx'] if request.POST['Vxx'] == "" else "")[0:100]

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def wyszukajkod(key):
    listakod = [("00-000", "12"), ("00-399", "05"), ("00-799", "12"), ("00-905", "05"), ("00-906", "12"),
                ("00-999", "12"), ("01-999", "12"), ("02-030", "05"), ("02-180", "12"), ("02-207", "05"),
                ("02-218", "12"), ("02-499", "05"), ("02-999", "20"), ("03-699", "14"), ("03-999", "14"),
                ("04-999", "14"), ("05-079", "12"), ("05-089", "05"), ("05-090", "20"), ("05-091", "12"),
                ("05-092", "20"), ("05-093", "12"), ("05-099", "20"), ("05-151", "12"), ("05-159", "20"),
                ("05-199", "14"), ("05-249", "20"), ("05-270", "14"), ("05-499", "05"), ("05-799", "12"),
                ("05-804", "05"), ("05-807", "12"), ("05-820", "05"), ("05-839", "12"), ("05-999", "20"),
                ("06-999", "14"), ("07-199", "20"), ("07-299", "14"), ("07-399", "20"), ("07-999", "14"),
                ("08-499", "32"), ("08-999", "20"), ("09-399", "20"), ("09-400", "20"), ("09-499", "23"),
                ("09-999", "17"), ("10-999", "17"), ("11-999", "17"), ("12-999", "17"), ("13-999", "17"),
                ("14-999", "41"), ("15-999", "41"), ("16-299", "17"), ("16-999", "41"), ("17-999", "41"),
                ("18-999", "41"), ("19-299", "17"), ("19-999", "32"), ("20-999", "32"), ("21-199", "14"),
                ("21-999", "32"), ("22-199", "14"), ("22-299", "32"), ("22-999", "32"), ("23-999", "32"),
                ("24-999", "15"), ("25-999", "15"), ("26-299", "23"), ("26-399", "15"), ("26-413", "05"),
                ("26-420", "15"), ("26-422", "05"), ("26-425", "15"), ("26-799", "05"), ("26-899", "32"),
                ("26-999", "15"), ("27-999", "15"), ("28-999", "15"), ("29-999", "06"), ("30-999", "06"),
                ("31-999", "06"), ("32-499", "18"), ("32-699", "06"), ("32-999", "06"), ("33-999", "06"),
                ("34-299", "40"), ("34-399", "06"), ("34-999", "09"), ("35-999", "09"), ("36-999", "09"),
                ("37-999", "09"), ("38-299", "06"), ("38-399", "09"), ("38-999", "09"), ("39-399", "15"),
                ("39-999", "18"), ("40-999", "18"), ("41-199", "25"), ("41-399", "18"), ("41-999", "25"),
                ("42-999", "18"), ("43-299", "40"), ("43-599", "18"), ("43-999", "40"), ("44-999", "04"),
                ("45-999", "04"), ("46-999", "04"), ("47-399", "40"), ("47-999", "04"), ("48-999", "04"),
                ("49-999", "02"), ("50-999", "24"), ("51-999", "02"), ("52-999", "02"), ("53-999", "02"),
                ("54-999", "02"), ("55-089", "24"), ("55-299", "10"), ("55-999", "10"), ("56-299", "24"),
                ("56-999", "02"), ("57-999", "02"), ("58-999", "10"), ("59-999", "01"), ("60-413", "31"),
                ("60-420", "01"), ("60-430", "31"), ("60-478", "01"), ("60-479", "31"), ("60-499", "01"),
                ("60-640", "31"), ("60-641", "01"), ("60-680", "31"), ("60-699", "01"), ("60-999", "19"),
                ("61-012", "31"), ("61-014", "19"), ("61-016", "31"), ("61-018", "19"), ("61-057", "31"),
                ("61-061", "19"), ("61-069", "31"), ("61-099", "01"), ("61-107", "19"), ("61-145", "16"),
                ("61-241", "19"), ("61-245", "16"), ("61-254", "19"), ("61-311", "16"), ("61-399", "01"),
                ("61-599", "31"), ("61-619", "01"), ("61-679", "31"), ("61-680", "01"), ("61-694", "31"),
                ("61-695", "01"), ("61-999", "31"), ("62-015", "19"), ("62-021", "16"), ("62-023", "19"),
                ("62-026", "31"), ("62-029", "01"), ("62-034", "16"), ("62-044", "01"), ("62-049", "16"),
                ("62-051", "01"), ("62-052", "16"), ("62-054", "01"), ("62-056", "16"), ("62-063", "01"),
                ("62-064", "16"), ("62-068", "01"), ("62-072", "16"), ("62-078", "01"), ("62-084", "31"),
                ("62-299", "19"), ("62-319", "16"), ("62-322", "19"), ("62-999", "16"), ("63-299", "19"),
                ("63-399", "24"), ("63-439", "19"), ("63-499", "24"), ("63-719", "16"), ("63-739", "24"),
                ("63-799", "16"), ("63-899", "24"), ("63-999", "16"), ("64-299", "01"), ("64-334", "16"),
                ("64-360", "31"), ("64-499", "31"), ("64-529", "01"), ("64-559", "31"), ("64-560", "01"),
                ("64-599", "31"), ("64-999", "13"), ("65-999", "13"), ("66-999", "13"), ("67-199", "10"),
                ("67-299", "13"), ("67-999", "13"), ("68-999", "13"), ("69-999", "13"), ("70-999", "13"),
                ("71-999", "13"), ("72-999", "13"), ("73-999", "13"), ("74-999", "07"), ("75-999", "07"),
                ("76-999", "07"), ("77-299", "55"), ("77-999", "07"), ("78-999", "07"), ("79-999", "03"),
                ("80-999", "07"), ("81-999", "03"), ("82-299", "17"), ("82-399", "03"), ("82-999", "03"),
                ("83-099", "17"), ("83-299", "07"), ("83-999", "07"), ("84-999", "55"), ("85-999", "55"),
                ("86-099", "11"), ("86-999", "11"), ("87-999", "55"), ("88-999", "55"), ("89-299", "31"),
                ("89-399", "55"), ("89-599", "07"), ("89-999", "08"), ("90-999", "08"), ("91-999", "08"),
                ("92-999", "08"), ("93-999", "08"), ("94-999", "08"), ("95-014", "23"), ("95-019", "08"),
                ("95-034", "23"), ("95-040", "08"), ("95-042", "23"), ("95-044", "08"), ("95-045", "23"),
                ("95-049", "08"), ("95-059", "23"), ("95-065", "08"), ("95-999", "23"), ("96-110", "05"),
                ("96-111", "23"), ("96-201", "05"), ("96-299", "23"), ("96-319", "05"), ("96-325", "23"),
                ("96-514", "12"), ("96-515", "23"), ("96-999", "23"), ("97-349", "25"), ("97-369", "23"),
                ("97-399", "08"), ("97-499", "25"), ("97-999", "08"), ("98-299", "25"), ("98-399", "24"),
                ("98-999", "23"), ("99-199", "08"), ("99-299", "23")]
    temp = bisect.bisect_left(listakod, (key,))
    return listakod[temp - 1][1]
