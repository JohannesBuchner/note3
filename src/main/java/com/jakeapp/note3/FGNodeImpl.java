package com.jakeapp.note3;

import java.util.List;
import java.util.Map;


public abstract class FGNodeImpl {

	protected List<FGNodeImpl> childrenImpl;

	protected FGNodeImpl parent;

	protected FGNode structure;

	public FGNodeImpl(FGNode structure, List<FGNodeImpl> childrenImpl) {
		this.structure = structure;
		this.childrenImpl = childrenImpl;
	}

	public abstract void applyStyle(Map<String, Object> style);

	public void setParent(FGNodeImpl impl) {
		this.parent = impl;
	}
}
