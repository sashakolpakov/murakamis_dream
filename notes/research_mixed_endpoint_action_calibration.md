# Absolute calibration of the ordinary endpoint action

Research proof, 5 November 2026. The ordinary endpoint action in the
contracted basis agrees with the original complete-edge wire action,
including its additive constant and the endpoint chirp. The identity
holds before taking a stationary value. Its specialization therefore
covers the whole private-leg rectangle used for the arbitrary open
three/four word. This does not identify the remaining vertex angles
or establish positivity of their geometric edge shapes.

## 1. The original primitives and their common chart

Use the original sine primitive
\[
 J(z)=\int_0^z\operatorname{Log}(2\sin\pi v)\,dv,
 \qquad J(0)=J(1/2)=0,                                  \tag{1}
\]
with its continuation from the real interval on \(0<\Re z<1\).
The complete ordinary boundary color is \(-2=-2\cos0\). Its
incidence phase and the endpoint phase from
[the original complete boundary sum](research_mixed_complete_boundary_sum.md)
are
\[
\begin{split}
 b(x,0)&=-2J(1/2-x)-2J(x),\\
 F(e,x)&=-2J(1/2-x)-3J(x)-J(e-x)+i\pi ex,\\
 \varphi(e)&=\frac\pi2(e-e^2).                           \tag{2}
\end{split}
\]
Here \(e\) is a private leg and \(x\) is the original adjacent
wire coordinate, not an angular filling variable.

Consider the connected convex domain
\[
 \mathcal D=\{(e,x)\in\mathbb C^2:
       0<\Re x<\Re e<1/2,\quad \Im x>0\}.               \tag{3}
\]
Set
\[
 X=e^{2\pi ix},\qquad U=e^{-2\pi ie},\qquad T=XU.
                                                                  \tag{4}
\]
On \(\mathcal D\), \(|X|<1\), \(\Im X>0\), and
\(\Im T<0\). In particular neither \(X\) nor \(T\)
meets the dilogarithm cut \([1,\infty)\). Define
\[
 I_X(e)=\frac{\operatorname{Li}_2(T)-\operatorname{Li}_2(X)}
                    {2\pi i},\qquad
 \ell_e(x)=2\pi iex-I_X(e)-\pi ix.                       \tag{5}
\]
The dilogarithm is the single-valued continuation of its disk series
to \(\mathbb C\setminus[1,\infty)\). These are precisely the
primitives of
[the original product interpolation](research_root_pochhammer_interpolation.md)
and [the absolute wire contraction](research_mixed_contracted_phase.md#5-absolute-action-under-the-exact-wire-contraction)
where \(|T|<1\). Formula (5) specifies their continuation on
\(\mathcal D\); it does not change a logarithmic lift.

Some points of \(\mathcal D\) can have \(|T|>1\). The
continuation in (5) is an identity of leading action primitives.
It does not extend the finite product interpolation or its
asymptotic theorem beyond the domain proved for that interpolation.

## 2. An identity before stationarity

**Theorem 1.** On \(\mathcal D\), with the branches just specified,
\[
 \boxed{\quad F(e,x)-i\varphi(e)=\ell_e(x)+b(x,0).\quad}  \tag{6}
\]
Both the complex additive constant and the logarithmic lifts in
this formula are fixed.

*Proof.* The following identities use the original sine logarithm
and the principal logarithms of \(1-X\), \(1+X\), and
\(1-T\):
\[
\begin{split}
 J'(x)&=\operatorname{Log}(1-X)+\frac{\pi i}{2}-\pi ix,\\
 J'(1/2-x)&=\operatorname{Log}(1+X)-\pi ix,\\
 J'(e-x)&=\operatorname{Log}(1-T)-\frac{\pi i}{2}
                                      +\pi i(e-x).       \tag{7}
\end{split}
\]
For the first two formulas, \(1\pm X\) have positive real
part. They follow from
\(2\sin\pi x=i e^{-\pi ix}(1-X)\) and
\(2\cos\pi x=e^{-\pi ix}(1+X)\), with their arguments
in the respective original sine strips. For the third, put
\(z=e-x\), so \(0<\Re z<1/2\). The identity
\(1-e^{-2\pi iz}=i e^{-\pi iz}2\sin\pi z\) gives the
displayed logarithm first for real \(z\in(0,1/2)\), then
throughout that connected vertical strip. Its left side always
has positive imaginary part. Thus none of (7) is only an equality
modulo \(2\pi i\).

Differentiating (5), using the same cut-plane logarithms, gives
\[
\begin{split}
 \partial_e\ell_e(x)&=2\pi ix-\operatorname{Log}(1-T),\\
 \partial_x\ell_e(x)&=2\pi ie+\operatorname{Log}(1-T)
                           -\operatorname{Log}(1-X)-\pi i.
                                                               \tag{8}
\end{split}
\]
The first and third lines of (7) now imply
\[
 \partial_e[F(e,x)-i\varphi(e)]
      =2\pi ix-\operatorname{Log}(1-T)
      =\partial_e[\ell_e(x)+b(x,0)].                       \tag{9}
\]
The three lines together give the exact common \(x\)-derivative
\[
\begin{split}
 \partial_xF(e,x)
 &=2\operatorname{Log}(1+X)-3\operatorname{Log}(1-X)
       +\operatorname{Log}(1-T)+2\pi ie-2\pi i\\
 &=\partial_x[\ell_e(x)+b(x,0)].                         \tag{10}
\end{split}
\]
Consequently the difference in (6) is constant on the connected
domain \(\mathcal D\).

To determine the constant, take \(x=r+ir^2\), \(e=2x\),
and let \(r\downarrow0\). This path lies in \(\mathcal D\)
for \(0<r<1/4\). The sine primitives at \(x\), \(e-x\),
and \(1/2-x\) tend to their normalized values at zero and
\(1/2\); all polynomial terms tend to zero. Thus the left
side and \(b(x,0)\) tend to zero. Also \(X\to1\) from
above and \(T=e^{-2\pi ix}\to1\) from below. The cut-plane
dilogarithm is continuous at \(1\), with value \(\pi^2/6\)
from both sides. Hence \(I_X(e)\to0\) and
\(\ell_e(x)\to0\). The constant is zero. \(\square\)

## 3. The whole certified private-leg image

Let
\[
 \mathcal E=[33/100,47/100]+i[-9/100,2/25],\qquad
 u_c(e)=\frac1\pi\arctan
                \frac{i+\sqrt{1-2e^{2\pi ie}}}{2},\qquad
 S(e)=F(e,u_c(e)).                                      \tag{11}
\]
The branch is the original one in
[the complete boundary theorem](research_complete_boundary_coefficient_asymptotic.md).
The certified instance in Section 4 of
[the endpoint packet extension](research_mixed_endpoint_packet_extension_criterion.md)
proves, on a neighborhood of the whole closed \(\mathcal E\),
\[
 F_x(e,u_c(e))=0,\qquad
 0<\Re u_c(e)<\Re e<1/2,\qquad \Im u_c(e)>0.             \tag{12}
\]
Its strict enclosures give a uniform separation from every boundary
in (3). Thus (6) specializes on that entire neighborhood to
\[
 \boxed{\quad
 C(e):=S(e)-i\varphi(e)
       =\ell_e(u_c(e))+b(u_c(e),0).
 \quad}                                                 \tag{13}
\]
Equation (10) also shows that \(u_c(e)\) is a stationary
wire for the right side, with the original zero logarithmic lift.
In particular the exact envelope derivative is
\[
 C'(e)=2\pi i u_c(e)
      -\operatorname{Log}\!\left(1-e^{2\pi i(u_c(e)-e)}\right).
                                                               \tag{14}
\]

The chirp in (13) is forced by the literal boundary change of basis:
the transformed vector contains
\[
 D_N(e)^{-1},\qquad
 D_N(e)=\exp\!\left(\frac{\pi i}{2}
                         [N(e-e^2)-e]\right)
       =e^{Ni\varphi(e)}e^{-\pi ie/2}.                  \tag{15}
\]
Thus its leading phase is \(S(e)-i\varphi(e)\), while
\(e^{\pi ie/2}\) stays in the original amplitude. This is
the normalization in
[the specified complex-index continuation](research_complete_boundary_complex_index.md),
equations (2)--(3), and holds at both level parities. No scalar
carrier, filling longitude, or trace normalization is changed by
the identity.

The same specialization holds on a neighborhood of the larger
\(E_{\mathrm{cap}}=[.27,.49]+i[-.055,.04]\). The certified
image in equation (9) of
[the endpoint cap-rectangle theorem](research_mixed_endpoint_cap_rectangle.md)
also satisfies every inequality in (3), so Theorem 1 gives (13)
there with exactly the same branches and zero additive constant.

This proves the endpoint action bridge only. Identifying an entire
localized mixed-word critical point with the marked positive
geometric solution still requires the separate vertex-angle maps,
their original lifted filling equations, and positivity of all
original edge shapes. Formula (13) alone makes no assertion about
those conditions or an arbitrary open-word integration cycle.
