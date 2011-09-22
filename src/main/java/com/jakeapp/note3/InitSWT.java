package com.jakeapp.note3;

import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Shell;

public class InitSWT {

	public static void main(String[] args) {
		Display d = new Display();
		Shell s = new Shell(d);
		Button b = new Button(s, 0);
		b.setVisible(true);
		s.pack();
	}
}
