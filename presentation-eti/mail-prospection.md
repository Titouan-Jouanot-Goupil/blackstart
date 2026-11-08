# Mail de prospection ETI

Premier contact avec une ETI, pour savoir si Black Start l'intéresse. But : obtenir une réponse (oui, non, pas maintenant) ou un échange de 30 minutes, pas vendre l'audit dès le premier mail.

**Destinataire :** DSI ou RSSI, à défaut le dirigeant (voir `docs/01-projet.md`).
**Pièce jointe :** `livrables/presentation-eti-black-start.pdf` (7 diapos).
**À remplir :** tout ce qui est entre crochets. Une phrase personnalisée sur l'entreprise vaut mieux que tout le reste du mail.

---

## Mail 1 : premier contact

**Objet** (au choix) :
- Sauriez-vous redémarrer [nom de l'entreprise] après une attaque ?
- Vos sauvegardes permettent vraiment une reprise d'activité ?
- Avis d'un DSI sur un projet de reprise après sinistre

> Bonjour [Madame / Monsieur] [Nom],
>
> Je suis [Prénom Nom], étudiant à [Télécom SudParis]. Avec quatre camarades de Télécom SudParis, de l'ENSIIE et d'IMT-BS, nous développons Black Start, un service pour les ETI qui veulent savoir si elles sauraient redémarrer leurs serveurs critiques après une cyberattaque ou une panne.
>
> [Phrase sur l'entreprise : par exemple « [Nom de l'entreprise] fait tourner [entrepôts / production / logistique] : un arrêt de quelques jours y coûte cher. »]
>
> Le constat de départ : la plupart des entreprises ont des sauvegardes, mais rarement la preuve qu'elles sauraient repartir, ni en combien de temps. Restaurer une image peut ramener la porte dérobée de l'attaquant ; un serveur qui redémarre ne veut pas dire que les commandes repartent.
>
> Black Start inventorie chaque serveur en lecture seule, le reconstruit à neuf dans un espace isolé avec vos données, puis vérifie par un test métier que l'activité repart. Sur notre prototype, un serveur de logistique est reconstruit et vérifié en 3 min 34 s, et la bascule vers la copie vérifiée coupe le service 28 s. L'analyse tourne chez vous : aucune donnée ne sort de votre infrastructure.
>
> Nous cherchons nos premières entreprises pilotes. Est-ce un sujet qui vous intéresse ? Un échange de 30 minutes nous aiderait déjà beaucoup, même si la réponse est « pas pour nous », pour comprendre comment vous gérez aujourd'hui vos sauvegardes et vos tests de reprise.
>
> Vous trouverez en pièce jointe une présentation de 7 pages.
>
> Bien cordialement,
>
> [Prénom Nom]
> Black Start · [Télécom SudParis]
> [téléphone] · [e-mail]
>
> *Si vous ne souhaitez plus recevoir de message de notre part, répondez simplement « stop ».*

---

## Mail 2 : relance, une semaine plus tard sans réponse

**Objet :** Re: [objet du premier mail]

> Bonjour [Madame / Monsieur] [Nom],
>
> Je me permets de revenir vers vous au sujet de Black Start. Une réponse courte me suffit : est-ce que la question « saurions-nous repartir, et en combien de temps ? » se pose chez [nom de l'entreprise] ?
>
> Si ce n'est pas vous qui suivez ce sujet, pourriez-vous m'indiquer la bonne personne ?
>
> Bien cordialement,
>
> [Prénom Nom]
> [téléphone]

Pas plus d'une relance.

---

## À ne pas faire

- **N'ajouter aucun client, partenaire ou résultat qui n'existe pas.** Tous les chiffres du mail sont mesurés sur notre banc de test (`docs/05-mesures.md`) ; dire « sur notre prototype », jamais « chez nos clients ».
- **Ne pas annoncer de prix dans le premier mail** : ils sont dans la présentation, et l'objectif ici est l'échange.
- **Ne pas écrire « conforme NIS2 »** : la loi Résilience qui transpose NIS2 n'est pas votée (voir `docs/04-marche-et-sources.md`).
- **Garder la ligne « stop ».** En prospection B2B, la CNIL admet l'e-mail sans consentement préalable si le message concerne le métier du destinataire, à condition de lui permettre de refuser simplement. À revérifier sur cnil.fr avant un envoi en nombre.

## Après une réponse

Noter chaque réponse (entreprise, fonction, date, ce qui a été dit) pour alimenter les entretiens du dossier. Un échange ne devient une « marque d'intérêt » dans un rendu qu'avec l'accord de la personne et une trace écrite.
