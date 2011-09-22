package com.jakeapp.note3;

import org.apache.log4j.Logger;

public class InitJython extends AbstractJythonInit {
	private static final Logger log = Logger.getLogger(InitJython.class);

	public InitJython(String[] args) {
		super(args);
	}

	public static void main(String[] args) {
		log.debug("Java started");
		new InitJython(args).run();
		log.debug("Java exiting");
	}

	public void run() {
	    /*Injector injector = Guice.createInjector(new ProjectModule());
	    c.set("injector", injector);
	    c.set("localProjectActions", injector.getInstance(LocalProjectActionsFactory.class));
	    c.set("connectProjectActions", injector.getInstance(ConnectProjectActionsFactory.class));
	    c.set("interactProjectActions", injector.getInstance(InteractProjectActionsFactory.class));
	    c.set("projectActions", injector.getInstance(ProjectActionsFactory.class));
	    c.set("contextFactory", injector.getInstance(ContextFactory.class));
		
		c.set("jythonConsole", c);
		c.set("jythonAppArgs", args);*/
		//c.exec("try:\n import sys\n import note3\n note3.main(sys.argv)\nexcept SystemExit: pass");
		//  c.execfile(InitJython.class.getResourceAsStream("mainwindow.py"));
		c.interact();
	}

}
