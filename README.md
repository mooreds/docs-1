# Transposit Docs

Docs are in `/docs/`.

Website is a static site generated with [Docusaurus](https://docusaurus.io) and hosted with Netlify.

Markdown docs ➞ Docusaurus build ➞ Netlify.

You can edit the docs by themselves and push changes to the master branch, without worrying about the website part, and a Netlify hook will build and do a production deploy automatically. Note that PRs and branches other than master do not have automatic preview deploys.

## Docusaurus

Website files are in `/website/`.

`npm run start` will spool up a local server at `http://localhost:3000`. `npm run build` will generate all the static files into `website/build`.

The nav is specified in [sidebars.json](website/sidebars.json). Other config is in [siteConfig.js](website/siteConfig.js).