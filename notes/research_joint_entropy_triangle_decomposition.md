# The joint one-sided score as three elementary concavity gaps

31 October 2026. Workspace research lemma, independently checked algebraically.
This supplies an exact identity for the new joint score. It does not establish
a global transport, a representation volume, or the universal inequality.

Use the [actual closed half-block entropy](actual_fejer_half_block_entropy.md).
For a LEFT degree vector write $\mu=q_b$, $\nu=1-q_c$, $w=\nu-\mu$,
$\xi=q_x$, $q_y=w-\xi$. The original interval coefficient entropy is

$$h=C(\alpha)-C(\beta),$$

where the input/output triangle allocations share their actual outer tilt and

$$
\alpha=(a,\mu,\tfrac12-\mu-a),\qquad
\beta=(b,\nu,\tfrac12-\nu-b),\qquad a-b=\xi.
$$

Here all triangle entries are nonnegative, $0\leq\xi\leq w$, and the
limiting endpoint allocations are those of the original coefficient formula.
The new local relative-energy bound has entropy

$$g=C(\gamma),\qquad \gamma=(\xi,\tfrac12-w,w-\xi).$$

Let $f(s)=[\Lambda(\pi s)+\Lambda(\pi/2-\pi s)]/\pi$ on $[0,1/2]$ and define

$$D_f(u,v)=f(u)+f(v)-f(u+v),\qquad u,v\geq0,\quad u+v\leq1/2.$$

Concavity and $f(0)=0$ imply $D_f\geq0$. The reflection identity is
$f(1/2-s)=f(s)$. Direct substitution now proves

$$
\boxed{\displaystyle
h+g=D_f(\tfrac12-a,\xi)+D_f(\mu,w)
                   +D_f(\mu+a,w-\xi).}
$$

Indeed, the three sums of arguments are $1/2-b$, $\nu$, and $\nu+b$;
all lie in $[0,1/2]$. Expanding their three differences gives

$$
f(a)-f(b)+f(\xi)
+f(\mu)-f(\nu)+f(w)
+f(\mu+a)-f(\nu+b)+f(w-\xi),
$$

which is $C(\alpha)-C(\beta)+C(\gamma)$ by reflection. Thus the joint
upper score $(h+g)/2$ is a half-sum of three nonnegative concavity gaps.
Each $D_f$ is also the sharp protected-outer spectral action from
[the boundary theorem](actual_protected_outer_spectral_energy.md).

The elementary reassociation identity

$$
D_f(u,v)+D_f(u+v,w)=D_f(v,w)+D_f(u,v+w)
$$

holds whenever the arguments and total stay in the domain. More generally,
any binary parenthesization of nonnegative leaves with total at most $1/2$
has total gap $\sum_i f(u_i)-f(\sum_i u_i)$. This is a telescoping identity,
not a claimed move of the original knot source.

A possible use is to reorganize interval pieces along the actual middle
forest while retaining all face targets. That application is still missing:
the identity does not itself prescribe the required reassignment of original
corner loads, preserve the original marked line flags, or compare the total
with the complete Casson--Rivin optimum. The prior obstruction to lossless
cover atomization of a fixed projected flow remains valid.

The local joint score is not concave in general. On a protected-outer row it
is $D_f(\mu,w)$, with $w$ fixed and $\nu=\mu+w$. Its second derivative in
$\mu$ is

$$
f''(\mu)-f''(\nu)
=-\frac{2\pi}{\sin(2\pi\mu)}
 +\frac{2\pi}{\sin(2\pi\nu)}.
$$

This is strictly positive when $0<\mu<\nu<1/2$ and $\mu+\nu>1/2$, for
example at $(\mu,\nu)=(3/10,2/5)$. Thus local concavity of $(h+g)/2$
cannot be used to infer the universal shared maximum. This is a local
curvature obstruction, not a feasible global-flow excess. Its first
$\mu$ derivative is always positive by strict concavity of $f$, which
still records a useful direction for a possible global transport.
