require 'securerandom'

module Jekyll
  class CollapseBlockTag < Liquid::Block

    def render(context)
      converter = context.registers[:site]
        .find_converter_instance(::Jekyll::Converters::Markdown)
      element_id = "collapsable-#{SecureRandom.hex}"

      <<-HTML
<div id="#{element_id}" class="collapsable collapsed">
  <a class="expand" href="javascript:document.getElementById('#{element_id}').classList.remove('collapsed')">
    ⊞ Expand code
  </a>
  <a class="collapse" href="javascript:document.getElementById('#{element_id}').classList.add('collapsed')">
    ⊟ Collapse code
  </a>
  #{converter.convert(super)}
</div>
      HTML
    end

  end
end

Liquid::Template.register_tag('collapse', Jekyll::CollapseBlockTag)
