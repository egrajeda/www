---
layout: post
title: "TypeScript with React: Components"
tags: [typescript, react]
updated: 2019-09-21
language: en
break: true
---

<p class="lead">
  The way I'm currently declaring components when working with TypeScript and React.
</p>

<hr />

To define a `React.Component<>` connected to Redux with properties and state:

{% collapse %}
```jsx
// updateTitle is a function defined in a separate file
interface IProps {
  updateTitle: typeof updateTitle;
  title: string;
}

interface IState {
  // ...
}

class MyComponent extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);

    this.state = { /* ... */ };

    this.onClick = this.onClick.bind(this);
  }

  onClick() {
    this.props.updateTitle("Updated title!");
  }

  render() {
    return (
      <div>
        <span>{this.props.title}</span>
      </div>
    );
  }
}

// TAppState should be replaced by the type of the global state
function mapStateToProps(state: TAppState) {
  return {
    title: state.title
  };
}

// TAction should be replaced with the type grouping the actions that can be
// bound
function mapDispatchToProps(dispatch: ThunkDispatch<any, any, TActions>) {
  return bindActionCreators(
    {
      updateTitle
    },
    dispatch
  );
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AdminEditPost);
```
{% endcollapse %}

## Conventions

* Methods that are meant to handle events should:
  * Start with `on` (e.g. `onSaveButtonClick`).
  * Be bound in the constructor to `this`, to avoid the arrow functions inside `render()`.
