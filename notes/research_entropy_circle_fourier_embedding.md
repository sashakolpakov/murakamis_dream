# A Fourier Hilbert representation of the local entropy defect

The entropy identity is not a quantum Plancherel theorem. A global application must impose the original shared face constraints.

Put \(\ell=1/2\) and

\[
 f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},
 \qquad 0\le t\le\ell.
\]

Here \(\Lambda(a)=-\int_0^a\log|2\sin u|\,du\). We have
\(f(0)=f(\ell)=0\), \(f(\ell-t)=f(t)\),
\(f'(t)=\log\cot(\pi t)\), and
\(f''(t)=-2\pi/\sin(2\pi t)<0\) in the interior. Extend \(f\)
periodically to \(\mathbb R/\ell\mathbb Z\).

## 1. Exact positive Fourier coefficients

For \(n\ge1\) write \(H_n^{\mathrm{odd}}=\sum_{j=1}^n(2j-1)^{-1}\).
Then the uniformly convergent identity is

\[
 \boxed{\displaystyle
 f(t)=\sum_{n=1}^{\infty}
       \frac{H_n^{\mathrm{odd}}}{\pi^2n^2}
       \bigl(1-\cos(4\pi nt)\bigr).}
 \tag{1}
\]

To check all constants, the cosine coefficient for period \(1/2\) is
\[
 a_n=4\int_0^{1/2}f(t)\cos(4\pi nt)\,dt
     =-\frac1{\pi^2n}\int_0^{\pi/2}
                     \log\cot x\,\sin(4nx)\,dx.
\]
Use the primitive \((1-\cos(4nx))/(4n)\) of \(\sin(4nx)\).
The logarithmic endpoint singularities have zero boundary product, so
\[
 I_n:=\int_0^{\pi/2}\log\cot x\,\sin(4nx)\,dx
 =\frac1{4n}\int_0^\pi\frac{1-\cos(2ny)}{\sin y}\,dy.
\]
If the last integral is \(J_n\), then \(J_0=0\) and
\[
 J_n-J_{n-1}=2\int_0^\pi\sin((2n-1)y)\,dy
            =\frac4{2n-1}.
\]
Thus \(I_n=H_n^{\mathrm{odd}}/n\) and
\(a_n=-H_n^{\mathrm{odd}}/(\pi^2n^2)\). Reflection makes the
sine coefficients zero. These coefficients are absolutely summable;
Fourier uniqueness and the value at zero fix the constant term and prove
(1). No asymptotic of a quantum coefficient is used here.

Let \(c_n=H_n^{\mathrm{odd}}/(\pi^2n^2)>0\). In the real Hilbert
space \(\ell^2(\mathbb N;\mathbb R^2)\), define
\[
 u(t)=\left(
 \sqrt{c_n/2}\,[\cos(4\pi nt)-1],\quad
 \sqrt{c_n/2}\,\sin(4\pi nt)
 \right)_{n\ge1}.
\]
Absolute summability proves that this is well defined, and directly
\[
 \|u(t)\|^2=f(t),\qquad
 \|u(t)-u(s)\|^2=f(t-s).                       \tag{2}
\]
In particular the periodic entropy kernel is conditionally negative
definite: for finitely many real \(r_i\) with \(\sum_i r_i=0\),
\[
 \sum_{i,j}r_ir_jf(t_i-t_j)
       =-2\left\|\sum_i r_i u(t_i)\right\|^2\le0.
\]

## 2. The actual one-sided score and the completion slack

Use the original half-block triangle allocations from
[the joint entropy identity](research_joint_entropy_triangle_decomposition.md):
\[
 \alpha=(a,\mu,\ell-\mu-a),\quad
 \beta=(b,\nu,\ell-\nu-b),\quad
 \xi=a-b,\quad w=\nu-\mu,
 \quad\gamma=(\xi,\ell-w,w-\xi).
\]
All entries are nonnegative; \(0\le\xi\le w\) and every triangle
has total \(\ell\). Set \(U(\alpha)=\bigoplus_{j=1}^3u(\alpha_j)\)
and \(C(\alpha)=\sum_jf(\alpha_j)\). Equations (1)--(2), together
with reflection of \(f\), give exactly
\[
 C(\alpha)=\|U(\alpha)\|^2,\quad
 C(\beta)=\|U(\beta)\|^2,\quad
 C(\gamma)=\|U(\alpha)-U(\beta)\|^2.           \tag{3}
\]
The pure triangle vertices all map to zero; this is not an injective
parameterization of the closed triangle simplex.

For the reference entropy \(h=C(\alpha)-C(\beta)\), local energy
bound \(g=C(\gamma)\), and joint upper score \(\widetilde h=(h+g)/2\),
we obtain
\[
 \boxed{\displaystyle
 \widetilde h
 =\langle U(\alpha),U(\alpha)-U(\beta)\rangle,
 \qquad
 \tau:=C(\alpha)-\widetilde h
 =\langle U(\alpha),U(\beta)\rangle.}          \tag{4}
\]
This identifies the local completion slack as an exact inner product,
not a guessed norm of a quantum state.

For completeness the nonnegative sign follows independently from the
elementary circular triangle inequality. Concavity and \(f(0)=0\) give
\(f(r+s)\le f(r)+f(s)\) for \(r,s\ge0\), \(r+s\le\ell\).
For \(0\le b\le a\le\ell\), reflection then gives
\[
 f(a-b)=f(\ell-a+b)\le f(\ell-a)+f(b)=f(a)+f(b).
\]
This proves the triangle inequality for the periodic kernel by choosing
representatives in \([0,\ell]\). Sum it over the three coordinates in
(3) to obtain \(\tau\ge0\). Its other orientation gives
\(\widetilde h\ge0\). Thus
\[
                  0\le\widetilde h\le C(\alpha).
\]

## 3. An exact transported closure for the angle constraints

Let \(R_s\) rotate the \(n\)-th real two-plane by \(4\pi ns\).
These operators form an orthogonal representation of
\(\mathbb R/\ell\mathbb Z\). Directly from the definition,
\[
 u(s+t)=u(s)+R_su(t).                              \tag{5}
\]
Consequently for any ordered list of real loads \(t_1,\ldots,t_m\),
\[
 u\left(\sum_{j=1}^m t_j\right)
 =\sum_{j=1}^m R_{t_1+\cdots+t_{j-1}}u(t_j).       \tag{6}
\]
An original face target one, or a triangle target \(1/2\), therefore
gives an exact zero on the right. The order may be the actual cyclic
incidence order. This is a transported linear closure, with the rotations
determined by the original partial angle sums. It is stronger information
than an untransported sum of vectors, which need not vanish.

This cocycle is explicitly a coboundary: with
\(v=(\sqrt{c_n/2},0)_{n\ge1}\), we have \(u(t)=R_tv-v\).
The vector \(v\) belongs to the Hilbert space. Thus the affine action
\(z\mapsto R_tz+u(t)\) has the fixed point \(-v\).
It would be incorrect to call this a nontrivial algebraic A-torsor or to
infer a quantum period from it. Its precise use is to encode the original
additive angle constraints by an explicit unitary transport, frequency
by frequency.

## 4. Scope of the Fourier reformulation

Equation (4) may organize the outer-transfer compensation in a Hilbert
space. It does not make the original nonlinear gluing constraints linear.
In particular, a face sum of angles does not make the untransported
sum of vectors \(u(t)\) vanish. It controls a product of phases and
the rotated sum in (6). Comparing those frames at different ports is
an additional problem. No cross-port orthogonality or Plancherel
contraction follows just from (4)--(6).
The inequality comparing the global shared score with the complete
hyperbolic volume is still open. This note records an exact representation
of its local defect, with no novelty claim about the general theory of
conditionally negative definite kernels.

## 5. A positive interval-cut realization of the same defect


The kernel also has a realization in which the local slack is a positive
intersection measure. Keep the circle length \(\ell=1/2\), and put
\(d(t)=\min(t,\ell-t)\) for \(0\le t\le\ell\). On
\(0<a<\ell/2\), define
\[
 w(a)=-f''(a)=\frac{2\pi}{\sin(2\pi a)}>0.
\]
Since \(f'(\ell/2)=0\), integration of the derivative gives
\[
 f(t)=f(d(t))=\int_0^{\ell/2}\min(d(t),a)w(a)\,da.       \tag{7}
\]
The integral converges because \(a w(a)\) is bounded near zero. For
each \(a\), let \(A_t^a=t+[0,a)\) in \(\mathbb R/\ell\mathbb Z\).
Normalized angular units are not used: circle measure is the ordinary
length \(ds\), with total \(\ell\). Direct interval geometry gives
\[
 |A_t^a\mathbin\triangle A_s^a|=2\min(d(t-s),a).
\]
On \((0,\ell/2)\times(\mathbb R/\ell\mathbb Z)\), use the positive
measure \(d\nu=\tfrac12w(a)\,da\,ds\), and set
\[
 v(a,s)=1_{A_0^a}(s),\qquad
 u_{\mathrm{cut}}(t)(a,s)=1_{A_t^a}(s)-1_{A_0^a}(s).
\]
Both functions belong to \(L^2(\nu)\):
\(\|v\|^2=\tfrac12\int_0^{\ell/2}a w(a)\,da<\infty\).
Equations (7) and the interval identity show
\[
 \|u_{\mathrm{cut}}(t)\|^2=f(t),\qquad
 \|u_{\mathrm{cut}}(t)-u_{\mathrm{cut}}(s)\|^2=f(t-s).           \tag{8}
\]
Translation of the circle variable gives the same unitary cocycle and
transported closure (5)--(6).

There is a useful pointwise feature beyond a generic Hilbert embedding.
For fixed \((a,s)\), all nonzero \(u_{\mathrm{cut}}(t)(a,s)\) have the SAME
sign: they are \(-1\) inside \(A_0^a\), and \(+1\) outside it. Write
\(E_t=\{(a,s):s\in A_t^a\mathbin\triangle A_0^a\}\). Then
\[
 u_{\mathrm{cut}}(t)u_{\mathrm{cut}}(s)=1_{E_t\cap E_s},\qquad
 u_{\mathrm{cut}}(t)\bigl(u_{\mathrm{cut}}(t)-u_{\mathrm{cut}}(s)\bigr)
                                      =1_{E_t\setminus E_s}.
\]
For the original endpoint triples \(\alpha,\beta\), equations (3)--(4)
therefore have the exact positive forms
\[
 \boxed{\displaystyle
 \tau=\sum_{j=1}^3\nu(E_{\alpha_j}\cap E_{\beta_j}),
 \qquad
 \widetilde h=\sum_{j=1}^3\nu(E_{\alpha_j}\setminus E_{\beta_j}).}
 \tag{9}
\]
These are finite measures even though the ambient measure \(\nu\) is
infinite. No hyperbolic solid or manifold volume is being assigned to the
sets \(E_t\). Equation (9) makes the local entropy defect a positive cut
quantity. A global comparison must still respect the original face loads
and the incidence-dependent transport frames; arbitrary independent cut
choices would enlarge the source and are not justified.
