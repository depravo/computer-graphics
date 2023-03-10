namespace colorPicker
{
    class ColorHolder
    {
        private RgbColor _rgbColor;
        private XyzColor _xyzColor;
        private CmykColor _cmykColor;

        public ColorHolder()
        {
            _rgbColor = new RgbColor(0, 0, 0);
			_xyzColor = new XyzColor(0, 0, 0);
            _cmykColor = new CmykColor(0, 0, 0, 1);
        }

        public RgbColor RgbColor
        {
            get => _rgbColor;
            set
            {
				_xyzColor.Update(value);
                _cmykColor.Update(value);
                _rgbColor = value;
            }
        }

        public XyzColor XyzColor
		{
            get => _xyzColor;
            set
            {
                _rgbColor.Update(value);
                _cmykColor.Update(_rgbColor);
				_xyzColor = value;
            }
        }

        public CmykColor CmykColor
        {
            get => _cmykColor;
            set
            {
                _rgbColor.Update(value);
				_xyzColor.Update(_rgbColor);
                _cmykColor = value;
            }
        }
    }
}
