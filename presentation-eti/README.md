# Présentation ETI

Présentation courte (7 diapos) à envoyer à une ETI prospect : problème, méthode, chiffres mesurés, livrable, offre, prochaine étape. Elle reprend le ton et la charte de la landing.

- `black-start-eti.html` : page autonome (polices et image intégrées), à ouvrir dans un navigateur.
- `../livrables/presentation-eti-black-start.pdf` : version PDF, une diapo par page.
- `mail-prospection.md` : mail de premier contact et relance, à envoyer avec le PDF.
- `prospects-eti.md` : première liste d'ETI à contacter, avec sources (8 nov. 2026).
- `source/` : une diapo par fichier (`slides/<id>.html`), ordre et titre dans `deck.json`.

Version en ligne, modifiable et exportable (PowerPoint, PDF) : https://claude.ai/artifact/YaDY3A4bSGRMX5KHfvkgTa. Elle est privée : la partager depuis son menu Share avant de l'envoyer.

## Reconstruire

```bash
python3 presentation-eti/source/build.py
node livrables/source/convertir.mjs eti
```

Une modification faite dans `source/` doit aussi être reportée dans la version en ligne, et inversement.

## Avant d'envoyer

- Diapo 7 : remplacer `[Nom · e-mail · téléphone]` par un vrai contact.
- Prix (diapo 6) : ceux du 7 novembre 2026 (audit 8–12 k€, migration 10–15 k€ par serveur, abonnement 500–900 € par mois et par application), alignés sur `analyse-marche-blackstart.md`.
