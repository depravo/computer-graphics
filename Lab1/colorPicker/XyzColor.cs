using System;

namespace colorPicker
{
    class XyzColor
    {
        public double X { get; private set; }
        public double Y { get; private set; }
        public double Z { get; private set; }

        public XyzColor(double x, double y, double z)
        {
            X = x;
            Y = y;
            Z = z;
        }

        public void Update(RgbColor rgb)
        {
			double r = (rgb.R / 255.0);
			double g = (rgb.G / 255.0);
			double b = (rgb.B / 255.0);
		
			if (r > 0.04045)
				r = Math.Pow(((r + 0.055) / 1.055), 2.4);
			else
				r = r / 12.92;
			if (g > 0.04045)
				g = Math.Pow(((g + 0.055) / 1.055), 2.4);
			else
				g = g / 12.92;
			if (b > 0.04045)
				b = Math.Pow(((b + 0.055) / 1.055), 2.4);
			else
				b = b / 12.92;
			r *= 100;
			g *= 100;
			b *= 100;
			X = Math.Floor(r * 0.412453 + g * 0.357580 + b * 0.180423);
			Y = Math.Floor(r * 0.212671 + g * 0.715160 + b * 0.072169);
			Z = Math.Floor(r * 0.019334 + g * 0.119193 + b * 0.950227);
		}
    }
}
