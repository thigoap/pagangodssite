module.exports = {
  content: ['../templates/*.html', 
            '../templates/pages/*.html'
          ],
  theme: {
    extend: {
      colors: {
        bgprimary: '#001426',
        bgsecondary: '#0c3556',
        textprimary: '#ffffff',
        textsecondary: '#20475c',
        texttertiary: '#f2ac08',
        btn01: '#f7c510',
        btn02: '#ef9e04'
      },
      gridTemplateColumns: {
        '00': 'repeat(auto-fill, minmax(160px, 1fr))',
        '01': 'repeat(auto-fit, minmax(160px, 1fr))',
      },
      backgroundImage: {
        'bg-pattern': "url('/static/images/background.jpg')"
      }

    },
  },
  plugins: [],
}
