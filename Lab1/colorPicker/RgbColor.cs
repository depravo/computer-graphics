using System;

namespace colorPicker
{
    class RgbColor
    {
        public double R { get; private set; }
        public double G { get; private set; }
        public double B { get; private set; }

        public RgbColor(double r, double g, double b)
        {
            R = r;
            G = g;
            B = b;
        }

        public void Update(XyzColor color)
        {
			var x = color.X / 100;
			var y = color.Y / 100;
			var z = color.Z / 100;

			var r = x * 3.2406 + y * -1.5372 + z * -0.4986;
			var g = x * -0.9689 + y * 1.8758 + z * 0.0415;
			var b = x * 0.0557 + y * -0.2040 + z * 1.0570;

			if (r > 0.0031308)
				r = 1.055 * (Math.Pow(r, (1 / 2.4))) - 0.055;
			else
				r *= 12.92;
			if (g > 0.0031308)
				g = 1.055 * (Math.Pow(g, (1 / 2.4))) - 0.055;
			else
				g *= 12.92;
			if (b > 0.0031308)
				b = 1.055 * (Math.Pow(b, (1 / 2.4))) - 0.055;
			else
				b *= 12.92;

			r *= 255;
			g *= 255;
			b *= 255;
			if (r <= 255 && r >= 0)
			{
				R = (byte)r;
			}

			if (g <= 255 && g >= 0)
			{
				G = (byte)g;
			}
			if (b <= 255 && b >= 0)
			{
				B = (byte)b;	
			}
		}

        public void Update(CmykColor color)
        {
            double cyan = color.C;
            double magenta = color.M;
            double yellow = color.Y;
            double black = color.K;

            R = Convert.ToByte((1 - Math.Min(1, cyan * (1 - black) + black)) * 255);
            G = Convert.ToByte((1 - Math.Min(1, magenta * (1 - black) + black)) * 255);
            B = Convert.ToByte((1 - Math.Min(1, yellow * (1 - black) + black)) * 255);
        }
    }
}
