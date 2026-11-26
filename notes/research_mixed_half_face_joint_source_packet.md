# The whole cap–conditional product near the incoming half face

Research corollary, 7 November 2026. The complete cap and complete
conditional packets at the half face combine on a genuine joint
complex neighborhood. The conditional continuation in the incoming
coordinate is proved here with its original finite row sets and
contour remainders. The reviewed half-face notes remain unchanged.

This identifies the leading contribution of the literal product.
It does not compare that product with the selected ordinary-next
affine action, deform the remaining incoming arc, or remove any
following conditional or Fourier factor. No numerical evaluation
or certificate replay is used.

## 1. The finite factors and the parameter set

Keep the exact definitions
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
 U_{0,N}(w,X)=\sum_{i=0}^{N-1}
                   H_N(w,r^{-i})\,p_i(X)/P_i,\\
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                   X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\\
 \mathcal Y=\left\{11/50\le\Re y\le9/20,\quad
                                      0\le\Im y\le1/100\right\}.
 \end{gathered}                                                    \tag{1}
\]
Every \(H_N\) is the whole original ordinary endpoint polynomial.
Both finite sums include all indices at both parities.

The [complete cap theorem](research_mixed_half_face_complete_cap_packet.md)
gives, on a fixed neighborhood of \((a,w)=(1/2,-2)\),
\[
 U_{0,N}(w,e^{-2\pi ia})
     =N^{-1}\mathcal B_{\rm cap}(a,w)
           e^{N\mathcal T(a,w)}
                    (1+O_{\rm hol}(N^{-1})),
                    \qquad \mathcal B_{\rm cap}\ne0 .
                                                               \tag{2}
\]
Its phase and coefficient are the original cap quantities
in equations (32)--(33) of that theorem.
The [complete conditional half-face theorem](research_mixed_half_face_complete_conditional_packet.md)
gives the whole second factor at \(a=1/2\), uniformly near
\(\mathcal Y\). We now continue the incoming coordinate of
that same finite factor.

## 2. Persistence of the complete conditional source

Use the original unmarked phase
\[
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat .
                                                               \tag{3}
\]
At \(a=1/2\), its selected critical point \(t_0(y)\) is
the unique original sheet proved in the conditional theorem.
It is holomorphic on a neighborhood of \(\mathcal Y\), and
\[
 \Re[-Q_{tt}(t_0(y);1/2,y)]>3\pi/25.
                                                               \tag{4}
\]
The same theorem proves uniform strict gaps for every
physical end, every alias current, and both main-path
connectors.

Fix once the positive collar \(\varepsilon\) and the
half-grid cuts from that proof:
\[
 \begin{gathered}
 L_N=\lfloor N/16\rfloor+1,\qquad
 K_N=\lceil N(1/2-\varepsilon)\rceil,\\
 \ell_N=(L_N-1/2)/N,\qquad u_N=(K_N-1/2)/N .
 \end{gathered}                                                    \tag{5}
\]
They do not move with \(a,y\). The incoming perturbation may
be restricted by \(|a-1/2|<\varepsilon/4\).
For all large \(N\), the exact interpolation
\[
 T_N(t;a,y)=e^{2\pi iNat}\Pi_N(a+t)\Pi_N(y+t)
                                E_N(a)E_N(y)E_N(t)^3
                                                               \tag{6}
\]
then remains in the original regular strips on the entire
fixed rectangle
\[
               \ell_N\le\Re t\le u_N,\qquad |\Im t|\le2.
                                                               \tag{7}
\]
In particular \(\Re(a+t)<1-\varepsilon/2\) after increasing
the lower threshold for \(N\) if necessary. All other
arguments have fixed compact margins from zero and one,
for \(y\) in a sufficiently small neighborhood of
\(\mathcal Y\). At every retained physical \(t=j/N\),
(6) is exactly the summand in (1).

We spell out persistence of the physical ends, where individual
numerators can revive after an incoming perturbation. Their
zero-safe real-index rate is
\[
 \begin{split}
 R(a,y;v)={}&-2\pi v\Im a-3J(v)\\
 &+\int_0^v\log|1-e^{-2\pi i(a+s)}|\,ds
  +\int_0^v\log|1-e^{-2\pi i(y+s)}|\,ds,
                       \qquad 0\le v\le1 .
 \end{split}                                                    \tag{8}
\]
The first term is the modulus of the original \(X^{-j}\)
carrier. The other two terms retain the full numerator
products, including their zeros.
On bounded parameter neighborhoods with nonzero \(X,Y\),
the integrated logarithms are jointly continuous in
\((a,y,v)\), uniformly for \(0\le v\le1\).
This follows from uniform local integrability of
\(\log|1-Re^{i\theta}|\) through \(R=1,\theta=0\).
The uniform finite-product upper estimates therefore give
\[
 \left|X^{-j}p_j(X)p_j(Y)/P_j^3\right|
       \le C N^B e^{NR(a,y;j/N)}
                                                               \tag{9}
\]
with a common polynomial prefactor on such neighborhoods.
One direct zero-safe justification is to regularize each
logarithm by
\(\frac12\log(|1-Re^{i\theta}|^2+N^{-2})\).
Its total variation is \(O(\log N)\); its integral differs
from the unregularized one by \(O(N^{-1})\), uniformly
for \(R\) in a fixed positive compact interval.
The finite sum is bounded above by the regularized sum,
so its upper error is \(O(\log N)\).
The sine-factorial denominator has the original uniform
\(O(\log N)\) error as well. Thus (9) does not use a
lower bound for any possibly vanishing numerator.

At \(a=1/2,y\in\mathcal Y\), the original end comparisons
put (8) below the real part of the critical action with
a common positive gap. The same is true on the fixed
collars used in (5). Compact continuity of (8) and of
the critical action preserves half that gap for the
entire low and high physical row sets after sufficiently
small complex parameter perturbations. Their at most
\(N\) rows add only a polynomial factor.
In particular the even-level rows which vanish at
\(X=-1\) are not deleted when \(a\ne1/2\).

For the central rows, the exact residue decomposition
is still
\[
 \begin{split}
 \sum_{j=L_N}^{K_N-1}T_N(j/N;a,y)
    &=N\int_{\ell_N}^{u_N}T_N(t;a,y)\,dt+\mathcal A_N(a,y),\\
 \mathcal A_N
    &=\frac{N}{2i}\left\{
       \int_{\partial\mathcal R_N^+}
               T_N(t)[\cot(\pi Nt)+i]\,dt+
       \int_{\partial\mathcal R_N^-}
               T_N(t)[\cot(\pi Nt)-i]\,dt\right\}.
 \end{split}                                                    \tag{10}
\]
The positive boundary orientations, both whole vertical
sign-halves, both horizontal aliases, and the density
\(+N\) are unchanged. All source factors on (7) are
uniformly regular. Consequently the strict gaps already
proved for the weighted alias phases persist by uniform
continuity of (3) on these bounded contours. No new
all-height curvature inequality is assumed after perturbing
\(a\).

The implicit function theorem applied to (4) supplies
a holomorphic critical point \(t(a,y)\) near \(t_0(y)\).
It is the unique root in the corresponding fixed local
neighborhoods. Uniform compact bounds permit a common
incoming radius and gluing on overlapping \(y\)-neighborhoods:
the local roots agree because they continue the same
simple sheet at \(a=1/2\).
To deform the main integral, first keep a fixed contour
through the base critical point in each such neighborhood.
The original unweighted connectors retain their strict
gaps. Translate a small central piece to the continued
critical point; its new short connectors lie in the
already gapped outer portion of that piece. Compactness
and the original strict horizontal curvature give uniform
gaps for these pieces also. This uses fixed base contours
when differentiating, not derivatives of a height graph.

Define
\[
 \begin{gathered}
 \Theta(a,y)=Q(t(a,y);a,y),\qquad
 a_0(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2},\\
 b(t;a,y)=
       \frac{a_0(a+t)a_0(y+t)}
                   {a_0(t)^3a_0(a)a_0(y)},\\
 \mathcal B_{\rm cond}(a,y)
       =\frac{\sqrt{2\pi}\,b(t(a,y);a,y)}
                           {\sqrt{-Q_{tt}(t(a,y);a,y)}} .
 \end{gathered}                                                    \tag{11}
\]
All factors and square roots have their original branches.
The factorial arguments remain regular, and (4) persists,
so \(\mathcal B_{\rm cond}\) is holomorphic and nonzero.

**Lemma 1.** There are an open neighborhood \(\mathcal V\)
of \(\mathcal Y\) and \(\rho_a>0\) on which the whole
finite conditional source satisfies
\[
 C_{1,N}(e^{-2\pi ia},e^{-2\pi iy})
   =N^{-1}\mathcal B_{\rm cond}(a,y)
                 e^{N\Theta(a,y)}
                        (1+O_{\rm hol}(N^{-1})),
                   \qquad |a-1/2|<\rho_a,\ y\in\mathcal V .
                                                               \tag{12}
\]
All fixed mixed \(a,y\)-derivatives of the normalized
relative error are \(O(N^{-1})\) on smaller neighborhoods.

The proof is the exact decomposition (9)--(10), the
continued Gaussian just described, and Cauchy's formula.
The original row \(N^{-3/2}\), density \(N\), and Gaussian
width \(N^{-1/2}\) give precisely \(N^{-1}\). There is
no additional \(\kappa_N\) or Fourier weight in (12).

## 3. The complete joint product

Shrink \(\rho_a\) and choose \(\rho_w>0\) so that the
complete cap expansion (2) holds on
\[
 |a-1/2|<\rho_a,\qquad |w+2|<\rho_w .
                                                               \tag{13}
\]
Put
\[
 \begin{split}
 \mathcal P(a,w,y)&=\mathcal T(a,w)+\Theta(a,y),\\
 \mathcal D(a,w,y)&=
              \mathcal B_{\rm cap}(a,w)\mathcal B_{\rm cond}(a,y).
 \end{split}                                                    \tag{14}
\]
Both functions are holomorphic, and \(\mathcal D\ne0\).

**Theorem 2.** On the product of (13) with \(\mathcal V\),
the literal complete factors satisfy
\[
 \boxed{\quad
 U_{0,N}(w,e^{-2\pi ia})\,
 C_{1,N}(e^{-2\pi ia},e^{-2\pi iy})
   =N^{-2}\mathcal D(a,w,y)e^{N\mathcal P(a,w,y)}
                         (1+O_{\rm hol}(N^{-1})).
 \quad}                                                        \tag{15}
\]
Every fixed mixed derivative of the normalized relative
error is \(O(N^{-1})\) on smaller product neighborhoods.
Both level parities and the original ordinary boundary
normals are retained.

Indeed multiply the two whole-source expansions (2)
and (12). Their nonzero symbols multiply; their relative
errors and all fixed derivatives remain \(O(N^{-1})\).
This multiplication makes no separate pointwise claim
about an unestimated contour piece: every remainder
was already paid for its complete finite factor.
The separate critical equations are the original
\(\Psi_e=0\) and \(Q_t=0\). At the half face their
joint private/index Hessian is diagonal; the same
decoupling holds at every fixed \(a\), since the two
factors have separate inner variables. Nonvanishing
therefore agrees with the product of their two
Gaussian coefficients.

The remaining selected source contains, in addition,
\[
 d_N(Y)Y^{-N}C_{\beta,N}(Y,Z),
                         \qquad \beta\in\{0,1\},
                                                               \tag{16}
\]
with its original outgoing weight when \(\beta=1\).
Equation (15) removes none of these factors and does
not integrate the shared coordinate \(a\).
In particular the inequality comparing
\(\Re\mathcal P\), the exact retained Fourier alternatives,
and the full next-source affine action is not proved
here. Neither a terminal-four action nor an arbitrary
uniform prefix ceiling is substituted for that target.
The remaining macroscopic incoming arc and its
prescribed vertical join also lie beyond the local
neighborhood (13).
