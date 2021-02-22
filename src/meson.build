klcc_sources = [
  'main.vala',
  'window.vala',
]

klcc_deps = [
  dependency('gio-2.0', version: '>= 2.50'),
  dependency('gtk+-3.0', version: '>= 3.22'),
]

gnome = import('gnome')

klcc_sources += gnome.compile_resources('klcc-resources',
  'klcc.gresource.xml',
  c_name: 'klcc'
)

executable('klcc', klcc_sources,
  vala_args: '--target-glib=2.50',  dependencies: klcc_deps,
  install: true,
)
