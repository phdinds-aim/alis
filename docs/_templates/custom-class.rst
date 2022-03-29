{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ name }}

   .. rubric:: Methods

   .. autosummary::
      :toctree: {{ name }}/
   {% for item in methods %}
      ~{{ name }}.{{ item }}
   {%- endfor %}