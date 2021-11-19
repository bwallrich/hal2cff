# # hal2cff example


from hal2cff import hal2cff
import ipywidgets as widgets


def on_button_clicked(_):
    print(text.value)
    print(hal2cff(text.value))
    widgets.HTML(
        value="<pre>{hal2cff(text.value))}</pre>",
        placeholder='Some HTML',
        description='Some HTML',
    )

text = widgets.Textarea(
    value='https://hal.archives-ouvertes.fr/hal-01361430v1',
    placeholder='Type something',
    description='String:',
    disabled=False
    )
text

button = widgets.Button(
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='vasy gros',
    icon='check' # (FontAwesome names without the `fa-` prefix)
    )
button.on_click( on_button_clicked )
button

# +
# print(hal2cff("https://hal.archives-ouvertes.fr/hal-01361430v1"))
# -










