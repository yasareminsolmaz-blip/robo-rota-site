"""Builds flockode/index.html (support) and flockode/privacy.html in six languages. Run: python3 build_flockode.py"""
import html

EMAIL = 'roborota.app@gmail.com'
UPDATED = '21.10.2026'
LANGS = [('en', 'English'), ('tr', 'Türkçe'), ('de', 'Deutsch'), ('es', 'Español'), ('nl', 'Nederlands'), ('fr', 'Français')]

CSS = """
:root{--paper:#12213A;--ink:#EBF1F6;--soft:#9FB2C6;--card:#1A2E4A;--line:#2F4A70;--accent:#F4BA4E;--loop:#82D48F}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{max-width:760px;margin:0 auto;padding:28px 16px 64px}
header{display:flex;align-items:center;gap:14px}
header img{width:64px;height:64px;border-radius:14px;border:1px solid var(--line)}
h1{font-size:30px;line-height:1.1;margin:0;color:#F6F1E4}
h1 span{color:var(--accent)}
.muted{color:var(--soft);margin:2px 0 0}
nav{display:flex;flex-wrap:wrap;gap:6px;margin:20px 0 4px}
nav a{border:1px solid var(--line);border-radius:999px;padding:3px 12px;background:var(--card);color:var(--ink);text-decoration:none;font-weight:700;font-size:14px}
nav a:hover{background:var(--accent);color:#2A1D05}
section{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:6px 20px 18px;margin-top:22px;box-shadow:0 10px 24px rgba(0,0,0,.28)}
h2{font-size:21px;margin:16px 0 6px;color:#F6F1E4}
h3{font-size:17px;margin:18px 0 4px;color:var(--loop)}
p,li{margin:6px 0}
a{color:var(--accent)}
.links{margin-top:10px;font-weight:700}
footer{margin-top:28px;color:var(--soft);font-size:14px;text-align:center}
"""

def page(title, subtitle, sections, other_link):
    nav = ''.join(f'<a href="#{c}">{n}</a>' for c, n in LANGS)
    body = ''.join(sections)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="icon" href="favicon.png">
<style>{CSS}</style>
</head>
<body>
<main>
  <header><img src="icon.png" alt=""><div><h1>Flock<span>ode</span></h1><p class="muted">{subtitle}</p></div></header>
  <nav>{nav}</nav>
  {body}
  <footer>{other_link} · © 2026 Yasar Emin Solmaz</footer>
</main>
</body>
</html>
"""

mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

# ---------------- Support page ----------------
SUPPORT = {
 'en': ('Support', [
  ('What is Flockode?', '<p>Flockode is a coding puzzle game for children aged 8–12. The child writes one program of IF → THEN rules, and every sheep in the flock runs it at the same time. Because the sheep start in different places, the code has to be truly general. Worlds 1–2 (20 levels) are free; a one-time purchase unlocks worlds 3–20 (180 levels).</p>'),
  ('Restoring the full version', '<p>On the Full Version screen tap <strong>Restore purchases</strong> and ask an adult to answer the parental question. The purchase is restored on every device signed in to the same Apple Account, and with Family Sharing on all family devices.</p>'),
  ('Why does the game ask a math question?', '<p>Buying, restoring and opening the App Store are protected by a parental gate so children cannot do them by themselves.</p>'),
  ('Language and sound', '<p>The game follows the device language. You can change it with the 🌐 button on the main screen. The speaker button turns the sheep sounds on or off; nothing plays when the device is muted.</p>'),
  ('Contact', f'<p>Questions, ideas or a level that seems impossible? Write to {mail}. We usually reply within a few days.</p>'),
 ]),
 'tr': ('Destek', [
  ('Flockode nedir?', '<p>Flockode, 8–12 yaş çocuklar için bir kodlama bulmacası oyunudur. Çocuk "EĞER → O ZAMAN" kurallarından oluşan tek bir kod yazar, sürüdeki bütün kuzular bu kodu aynı anda çalıştırır. Kuzular farklı yerlerden başladığı için kodun gerçekten genel olması gerekir. Dünya 1–2 (20 seviye) ücretsizdir. Tek seferlik bir satın alma Dünya 3–20\'yi (180 seviye) açar.</p>'),
  ('Tam sürümü geri yükleme', '<p>Tam sürüm ekranında <strong>Satın alımları geri yükle</strong>\'ye dokunun ve ebeveyn sorusunu bir yetişkine yanıtlatın. Satın alma, aynı Apple hesabıyla giriş yapılmış tüm cihazlarda; Aile Paylaşımı açıksa ailedeki tüm cihazlarda geri gelir.</p>'),
  ('Oyun neden matematik sorusu soruyor?', '<p>Satın alma, geri yükleme ve App Store\'u açma, çocukların bunları tek başına yapamaması için ebeveyn kontrolüyle korunur.</p>'),
  ('Dil ve ses', '<p>Oyun cihazın dilini kullanır. Ana ekrandaki 🌐 düğmesiyle değiştirebilirsiniz. Hoparlör düğmesi kuzu seslerini açıp kapatır. Cihaz sessizdeyse ses çalmaz.</p>'),
  ('İletişim', f'<p>Soru, öneri ya da çözülemiyor gibi görünen bir seviye mi var? {mail} adresine yazın. Genellikle birkaç gün içinde yanıt veriyoruz.</p>'),
 ]),
 'de': ('Hilfe', [
  ('Was ist Flockode?', '<p>Flockode ist ein Programmier-Rätselspiel für Kinder von 8 bis 12 Jahren. Das Kind schreibt ein Programm aus WENN → DANN-Regeln, und alle Schafe der Herde führen es gleichzeitig aus. Weil die Schafe an verschiedenen Stellen starten, muss der Code wirklich allgemein sein. Welt 1–2 (20 Level) sind kostenlos; ein einmaliger Kauf schaltet Welt 3–20 (180 Level) frei.</p>'),
  ('Vollversion wiederherstellen', '<p>Tippe auf dem Vollversion-Bildschirm auf <strong>Käufe wiederherstellen</strong> und lass einen Erwachsenen die Elternfrage beantworten. Der Kauf wird auf allen Geräten mit demselben Apple Account wiederhergestellt, mit Familienfreigabe auf allen Geräten der Familie.</p>'),
  ('Warum fragt das Spiel nach einer Rechenaufgabe?', '<p>Kaufen, Wiederherstellen und das Öffnen des App Store sind durch eine Elternkontrolle geschützt, damit Kinder das nicht allein tun können.</p>'),
  ('Sprache und Ton', '<p>Das Spiel nutzt die Gerätesprache. Mit der 🌐-Taste auf dem Hauptbildschirm kannst du sie ändern. Die Lautsprecher-Taste schaltet die Schafgeräusche an oder aus; bei stummgeschaltetem Gerät ist nichts zu hören.</p>'),
  ('Kontakt', f'<p>Fragen, Ideen oder ein Level, das unlösbar scheint? Schreib an {mail}. Wir antworten meist innerhalb weniger Tage.</p>'),
 ]),
 'es': ('Ayuda', [
  ('¿Qué es Flockode?', '<p>Flockode es un juego de rompecabezas de programación para niños de 8 a 12 años. El niño escribe un programa de reglas SI → ENTONCES y todas las ovejas del rebaño lo ejecutan a la vez. Como las ovejas empiezan en lugares distintos, el código tiene que ser realmente general. Los mundos 1–2 (20 niveles) son gratis; una compra única desbloquea los mundos 3–20 (180 niveles).</p>'),
  ('Restaurar la versión completa', '<p>En la pantalla de la versión completa toca <strong>Restaurar compras</strong> y pide a un adulto que responda la pregunta parental. La compra se restaura en todos los dispositivos con la misma cuenta de Apple y, con En familia, en todos los dispositivos de la familia.</p>'),
  ('¿Por qué el juego hace una pregunta de matemáticas?', '<p>Comprar, restaurar y abrir el App Store están protegidos por un control parental para que los niños no puedan hacerlo solos.</p>'),
  ('Idioma y sonido', '<p>El juego usa el idioma del dispositivo. Puedes cambiarlo con el botón 🌐 de la pantalla principal. El botón del altavoz activa o desactiva los sonidos de las ovejas; no suena nada si el dispositivo está en silencio.</p>'),
  ('Contacto', f'<p>¿Preguntas, ideas o un nivel que parece imposible? Escribe a {mail}. Solemos responder en pocos días.</p>'),
 ]),
 'nl': ('Hulp', [
  ('Wat is Flockode?', '<p>Flockode is een programmeerpuzzelspel voor kinderen van 8 tot 12 jaar. Het kind schrijft één programma met ALS → DAN-regels en alle schapen van de kudde voeren het tegelijk uit. Omdat de schapen op verschillende plekken beginnen, moet de code echt algemeen zijn. Wereld 1–2 (20 levels) zijn gratis; een eenmalige aankoop opent wereld 3–20 (180 levels).</p>'),
  ('De volledige versie herstellen', '<p>Tik op het scherm Volledige versie op <strong>Aankopen herstellen</strong> en laat een volwassene de ouderlijke vraag beantwoorden. De aankoop wordt hersteld op elk apparaat met hetzelfde Apple-account, en met Delen met gezin op alle apparaten van het gezin.</p>'),
  ('Waarom stelt het spel een rekensom?', '<p>Kopen, herstellen en de App Store openen zitten achter een ouderlijk slot, zodat kinderen dat niet alleen kunnen doen.</p>'),
  ('Taal en geluid', '<p>Het spel volgt de taal van het apparaat. Je kunt die wijzigen met de 🌐-knop op het hoofdscherm. De luidsprekerknop zet de schapengeluiden aan of uit; als het apparaat op stil staat, is er niets te horen.</p>'),
  ('Contact', f'<p>Vragen, ideeën of een level dat onmogelijk lijkt? Schrijf naar {mail}. We antwoorden meestal binnen een paar dagen.</p>'),
 ]),
 'fr': ('Assistance', [
  ('Qu’est-ce que Flockode ?', '<p>Flockode est un jeu de casse-tête de programmation pour les enfants de 8 à 12 ans. L’enfant écrit un programme de règles SI → ALORS et tous les moutons du troupeau l’exécutent en même temps. Comme les moutons partent d’endroits différents, le code doit être vraiment général. Les mondes 1–2 (20 niveaux) sont gratuits ; un achat unique débloque les mondes 3–20 (180 niveaux).</p>'),
  ('Restaurer la version complète', '<p>Sur l’écran Version complète, touche <strong>Restaurer les achats</strong> et demande à un adulte de répondre à la question parentale. L’achat est restauré sur tous les appareils connectés au même compte Apple et, avec le Partage familial, sur tous les appareils de la famille.</p>'),
  ('Pourquoi le jeu pose-t-il une question de calcul ?', '<p>Les achats, la restauration et l’ouverture de l’App Store sont protégés par un contrôle parental pour que les enfants ne puissent pas le faire seuls.</p>'),
  ('Langue et son', '<p>Le jeu suit la langue de l’appareil. Tu peux la changer avec le bouton 🌐 de l’écran principal. Le bouton haut-parleur active ou coupe les bruits des moutons ; rien ne joue quand l’appareil est en mode silencieux.</p>'),
  ('Contact', f'<p>Des questions, des idées ou un niveau qui semble impossible ? Écris à {mail}. Nous répondons généralement en quelques jours.</p>'),
 ]),
}
PRIV_LINK = {'en': 'Privacy Policy', 'tr': 'Gizlilik Politikası', 'de': 'Datenschutzerklärung', 'es': 'Política de privacidad', 'nl': 'Privacybeleid', 'fr': 'Politique de confidentialité'}
SUPPORT_LINK = {'en': 'Support', 'tr': 'Destek', 'de': 'Hilfe', 'es': 'Ayuda', 'nl': 'Hulp', 'fr': 'Assistance'}

def support_sections():
    out = []
    for code, name in LANGS:
        title, items = SUPPORT[code]
        inner = ''.join(f'<h3>{html.escape(h)}</h3>{b}' for h, b in items)
        out.append(f'<section id="{code}" lang="{code}"><h2>{name} · {title}</h2>{inner}<p class="links"><a href="privacy.html#{code}">{PRIV_LINK[code]} →</a></p></section>')
    return out

# ---------------- Privacy policy ----------------
PRIVACY = {
 'en': [
  ('Summary', 'Flockode collects no personal data. There are no accounts, no ads, no analytics and no tracking, and the game works offline.'),
  ('Data stored on the device', 'The game saves progress (stars and unlocked levels), the sound setting, the chosen language and whether the full version is unlocked. This data stays on the device, is never sent to us or to anyone else, and is deleted when the app is removed.'),
  ('Purchases', 'The full version is sold through Apple\'s In-App Purchase system. Apple processes the payment; we never see payment details, the Apple Account or any personal information. Purchases are behind a parental gate.'),
  ('Children', 'The game is made for children aged 8–12 and is designed to follow the App Store Kids Category rules, the U.S. Children\'s Online Privacy Protection Act (COPPA) and the GDPR. Because we collect no personal data, no personal data of children is collected, shared or sold.'),
  ('Third parties', 'The app contains no third-party advertising, analytics or social media services. The only link that leaves the app opens our other game\'s App Store page, and it is behind a parental gate.'),
  ('Changes and contact', f'If this policy changes, the new version will be posted on this page with a new date. Questions: {mail}.'),
 ],
 'tr': [
  ('Özet', 'Flockode hiçbir kişisel veri toplamaz. Hesap, reklam, analiz ve izleme (tracking) yoktur. Oyun internetsiz çalışır.'),
  ('Cihazda saklanan veriler', 'Oyun ilerlemeyi (yıldızlar ve açılan seviyeler), ses ayarını, seçilen dili ve tam sürümün açık olup olmadığını kaydeder. Bu veriler cihazda kalır, bize ya da başka birine gönderilmez ve uygulama silinince silinir.'),
  ('Satın almalar', 'Tam sürüm Apple\'ın uygulama içi satın alma sistemiyle satılır. Ödemeyi Apple işler. Ödeme bilgilerini, Apple hesabını ya da herhangi bir kişisel bilgiyi biz hiçbir zaman görmeyiz. Satın almalar ebeveyn kontrolünün arkasındadır.'),
  ('Çocuklar', 'Oyun 8–12 yaş çocuklar için yapılmıştır ve App Store Çocuklar kategorisi kurallarına, ABD Çocukların Çevrim İçi Gizliliğini Koruma Yasası\'na (COPPA), GDPR\'a ve KVKK\'ya uygun olacak şekilde tasarlanmıştır. Kişisel veri toplamadığımız için çocuklara ait hiçbir kişisel veri toplanmaz, paylaşılmaz ya da satılmaz.'),
  ('Üçüncü taraflar', 'Uygulamada üçüncü taraf reklam, analiz ya da sosyal medya hizmeti yoktur. Uygulamanın dışına çıkan tek bağlantı diğer oyunumuzun App Store sayfasını açar ve ebeveyn kontrolünün arkasındadır.'),
  ('Değişiklikler ve iletişim', f'Bu politika değişirse yeni sürüm yeni tarihle bu sayfada yayınlanır. Sorularınız için: {mail}.'),
 ],
 'de': [
  ('Zusammenfassung', 'Flockode erhebt keine personenbezogenen Daten. Es gibt keine Konten, keine Werbung, keine Analyse und kein Tracking; das Spiel funktioniert offline.'),
  ('Auf dem Gerät gespeicherte Daten', 'Das Spiel speichert den Fortschritt (Sterne und freigeschaltete Level), die Toneinstellung, die gewählte Sprache und ob die Vollversion freigeschaltet ist. Diese Daten bleiben auf dem Gerät, werden weder an uns noch an Dritte gesendet und beim Löschen der App entfernt.'),
  ('Käufe', 'Die Vollversion wird über Apples In-App-Kauf verkauft. Apple wickelt die Zahlung ab; wir sehen weder Zahlungsdaten noch den Apple Account oder andere persönliche Informationen. Käufe sind durch eine Elternkontrolle geschützt.'),
  ('Kinder', 'Das Spiel richtet sich an Kinder von 8 bis 12 Jahren und ist so gestaltet, dass es den Regeln der App-Store-Kategorie „Kinder“, dem US-amerikanischen COPPA und der DSGVO entspricht. Da wir keine personenbezogenen Daten erheben, werden keine Daten von Kindern erhoben, weitergegeben oder verkauft.'),
  ('Dritte', 'Die App enthält keine Werbe-, Analyse- oder Social-Media-Dienste von Dritten. Der einzige Link aus der App öffnet die App-Store-Seite unseres anderen Spiels und ist durch eine Elternkontrolle geschützt.'),
  ('Änderungen und Kontakt', f'Wenn sich diese Erklärung ändert, wird die neue Fassung mit neuem Datum auf dieser Seite veröffentlicht. Fragen: {mail}.'),
 ],
 'es': [
  ('Resumen', 'Flockode no recoge ningún dato personal. No hay cuentas, anuncios, analíticas ni seguimiento, y el juego funciona sin conexión.'),
  ('Datos guardados en el dispositivo', 'El juego guarda el progreso (estrellas y niveles desbloqueados), el ajuste de sonido, el idioma elegido y si la versión completa está desbloqueada. Estos datos se quedan en el dispositivo, nunca se envían a nosotros ni a nadie, y se borran al eliminar la app.'),
  ('Compras', 'La versión completa se vende mediante las compras dentro de la app de Apple. Apple procesa el pago; nunca vemos los datos de pago, la cuenta de Apple ni ninguna información personal. Las compras están protegidas por un control parental.'),
  ('Niños', 'El juego está pensado para niños de 8 a 12 años y está diseñado para cumplir las normas de la categoría Niños del App Store, la ley estadounidense COPPA y el RGPD. Como no recogemos datos personales, no se recogen, comparten ni venden datos de niños.'),
  ('Terceros', 'La app no contiene servicios de publicidad, analítica ni redes sociales de terceros. El único enlace que sale de la app abre la página del App Store de nuestro otro juego y está protegido por un control parental.'),
  ('Cambios y contacto', f'Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha. Preguntas: {mail}.'),
 ],
 'nl': [
  ('Samenvatting', 'Flockode verzamelt geen persoonsgegevens. Er zijn geen accounts, geen advertenties, geen analyses en geen tracking, en het spel werkt offline.'),
  ('Gegevens op het apparaat', 'Het spel bewaart de voortgang (sterren en geopende levels), de geluidsinstelling, de gekozen taal en of de volledige versie is ontgrendeld. Deze gegevens blijven op het apparaat, worden nooit naar ons of anderen gestuurd en worden verwijderd als de app wordt verwijderd.'),
  ('Aankopen', 'De volledige versie wordt verkocht via de in-app-aankopen van Apple. Apple verwerkt de betaling; wij zien nooit betaalgegevens, het Apple-account of andere persoonlijke informatie. Aankopen zitten achter een ouderlijk slot.'),
  ('Kinderen', 'Het spel is gemaakt voor kinderen van 8 tot 12 jaar en is ontworpen om te voldoen aan de regels van de App Store-categorie Kinderen, de Amerikaanse COPPA en de AVG. Omdat we geen persoonsgegevens verzamelen, worden er geen gegevens van kinderen verzameld, gedeeld of verkocht.'),
  ('Derden', 'De app bevat geen advertentie-, analyse- of socialemediadiensten van derden. De enige link die de app verlaat, opent de App Store-pagina van ons andere spel en zit achter een ouderlijk slot.'),
  ('Wijzigingen en contact', f'Als dit beleid verandert, verschijnt de nieuwe versie met een nieuwe datum op deze pagina. Vragen: {mail}.'),
 ],
 'fr': [
  ('Résumé', "Flockode ne collecte aucune donnée personnelle. Pas de compte, pas de publicité, pas d'analyse ni de suivi, et le jeu fonctionne hors ligne."),
  ("Données enregistrées sur l'appareil", "Le jeu enregistre la progression (étoiles et niveaux débloqués), le réglage du son, la langue choisie et l'état de la version complète. Ces données restent sur l'appareil, ne sont jamais envoyées ni à nous ni à personne, et sont supprimées avec l'app."),
  ('Achats', "La version complète est vendue via les achats intégrés d'Apple. Apple traite le paiement ; nous ne voyons jamais les données de paiement, le compte Apple ni aucune information personnelle. Les achats sont protégés par un contrôle parental."),
  ('Enfants', "Le jeu est conçu pour les enfants de 8 à 12 ans et respecte les règles de la catégorie Enfants de l'App Store, la loi américaine COPPA et le RGPD. Comme nous ne collectons aucune donnée personnelle, aucune donnée d'enfant n'est collectée, partagée ou vendue."),
  ('Tiers', "L'app ne contient aucun service tiers de publicité, d'analyse ou de réseau social. Le seul lien qui sort de l'app ouvre la page App Store de notre autre jeu et il est protégé par un contrôle parental."),
  ('Modifications et contact', f'Si cette politique change, la nouvelle version sera publiée sur cette page avec une nouvelle date. Questions : {mail}.'),
 ],
}
UPDATED_LABEL = {'en': 'Last updated', 'tr': 'Son güncelleme', 'de': 'Zuletzt aktualisiert', 'es': 'Última actualización', 'nl': 'Laatst bijgewerkt', 'fr': 'Dernière mise à jour'}

def privacy_sections():
    out = []
    for code, name in LANGS:
        inner = ''.join(f'<h3>{html.escape(h)}</h3><p>{b}</p>' for h, b in PRIVACY[code])
        out.append(f'<section id="{code}" lang="{code}"><h2>{name} · {PRIV_LINK[code]}</h2><p class="muted">{UPDATED_LABEL[code]}: {UPDATED}</p>{inner}<p class="links"><a href="index.html#{code}">{SUPPORT_LINK[code]} →</a></p></section>')
    return out

open('flockode/index.html', 'w').write(page('Flockode – Support', 'Coding puzzles for kids · Support', support_sections(), '<a href="privacy.html">Privacy Policy</a>'))
open('flockode/privacy.html', 'w').write(page('Flockode – Privacy Policy', 'Privacy Policy', privacy_sections(), '<a href="index.html">Support</a>'))
print('built flockode')
