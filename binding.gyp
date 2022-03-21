{
  'targets': [
    {
      'target_name': 'arl-dilithium-native',
      'sources': [ 'src/arl_dilithium.cc' ,
		                'src/dilithium3/ntt.c',
		                'src/dilithium3/packing.c',
		                'src/dilithium3/poly.c',
                    'src/dilithium3/polyvec.c',
                    'src/dilithium3/reduce.c',
                    'src/dilithium3/rounding.c',
                    'src/dilithium3/sign.c',
                    'src/dilithium3/symmetric-shake.c',
                    'src/dilithium3/randombytes.c',
                    'src/dilithium3/fips202.c',
      ],
      'include_dirs': ["<!@(node -p \"require('node-addon-api').include\")"],
      'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7'
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      }
    }
  ]
}