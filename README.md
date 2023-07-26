![tests](https://github.com/torchbox/wagtail-jotform/workflows/Tests/badge.svg)
[![codecov](https://codecov.io/gh/kevinhowbrook/wagtail-jotform/branch/master/graph/badge.svg?token=GBDM9H1A2X)](https://codecov.io/gh/kevinhowbrook/wagtail-jotform)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Total alerts](https://img.shields.io/lgtm/alerts/g/kevinhowbrook/wagtail-jotform.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kevinhowbrook/wagtail-jotform/alerts/)

# Wagtail Jotform

Embedable [Jotform](https://www.jotform.com) forms for Wagtail pages.

Wagtail Jotform works by providing a new `EmbeddedFormPage` page type with a form choice field. Values for this form field are populated from the Jotform API.

## Installation

Install from [pypi](https://pypi.org/project/wagtail-jotform/):

```bash
pip install wagtail-jotform
```

## Configuration

You will need an API key from Jotform. Add the following variables to your settings:

```python
WAGTAIL_JOTFORM = {
    "API_KEY": "somekey",
    "API_URL": "https://api.jotform.com",
    "LIMIT": 50,
}
```

`LIMIT` is the number of results in each result set for form list. Default is 50. Maximum is 1000.

If your Jotform account is in [EU safe mode](https://www.jotform.com/eu-safe-forms/), your `JOTFORM_API_URL` should be `https://eu-api.jotform.com`.

Add the following to your `INSTALLED_APPS` in settings, and note that `wagtail_jotform` depends on `routable_page`:

```python
INSTALLED_APPS = [
    ...
    "wagtail_jotform",
    "wagtail.contrib.routable_page",
]
```

## Thank you page

Thank you pages work via Wagtail's [RoutablePageMixin](https://docs.wagtail.io/en/latest/reference/contrib/routablepage.html).

When a form is created, the Jotform `thankurl` is set with your created form's thank you page URL, e.g. `https://mysite.com/formpage/thank-you`. When the form is submitted, the user will be redirected accordingly and be show the 'thank you' data specified on on the form page added.

## Overriding templates

Wagtail Jotform has two templates:

- embedded_form_page.html
- thank_you.html

You can override these templates in your project by adding them in the following location:

- your_project_root/
  - templates/
    - wagtail_jotform/
      - embed_form_page.html
      - thank_you.html

## Contributing

We welcome contributions to this project. Please follow the [contributing instructions](docs/CONTRIBUTING.md) to get started.

## Release process

To release a new version, the [Release documentation](docs/RELEASE.md) should be followed.
