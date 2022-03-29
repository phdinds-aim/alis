{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ name }}

   .. rubric:: Methods

   .. autosummary::
      :toctree:
   {% for item in methods %}
      ~{{ name }}.{{ item }}
   {%- endfor %}