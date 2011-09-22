package com.jakeapp.note3;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;


public class FGNode {

	private final List<FGNode> children = new LinkedList<FGNode>();

	private FGNode parent_node = null;

	private final Map<String, Object> properties = new HashMap<String, Object>();

	public FGNode() {

	}

	public FGNode(Map<String, Object> properties) {
		this.properties.putAll(properties);
	}

	public FGNode(Map<String, Object> properties, List<FGNode> children) {
		this(properties);
		for (FGNode c : children) {
			this.addChild(c);
			c.setParent(this);
		}
	}

	public void addChild(FGNode c) {
		this.children.add(c);
	}

	public void removeChild(FGNode c) {
		this.children.remove(c);
	}

	public void setProperty(FGNode c) {
		this.children.add(c);
	}

	public void setParent(FGNode parent_node) {
		this.parent_node = parent_node;
	}

}
