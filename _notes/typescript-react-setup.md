---
layout: post
title: "TypeScript with React: Setup"
tags: [typescript, react, setup]
updated: 2019-09-05
language: en
---

<p class="lead">
  A handy setup to use when working with TypeScript and React.
</p>

<hr />

Use [Create React App](https://create-react-app.dev) to create the project:
```
$ create-react-app <name> --typescript
```

Use [Prettier](https://prettier.io) to prettify the code:
```
$ yarn add prettier --dev --exact
$ yarn run prettier --write src/**/*.tsx
```
