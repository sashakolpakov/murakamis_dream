# The complete Fourier sources after one and two negative crossings

Research deduction, 7 November 2026. The two negative crossings can
be performed on the whole original Fourier boundary, without selecting
its first coefficient. One negative crossing gives the Fourier
transform of the original type-three conditional source. Two negative
crossings collapse to one literal type-three conditional polynomial,
with an explicit chirp and scalar.

The identities hold at every level and both parities. They retain
all Fourier channels and the original crossing matrix. They do not
assert that the new conditional parameters lie in an already proved
packet domain. No numerical evaluation is used.

## 1. Conventions and the full coefficient dictionary

Put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad r=Q^{-1},
 \quad \kappa=q^{D^2/2},\qquad N\ge2,
\]
\[
 P_j=(r;r)_j,\quad F_j=(Q;Q)_j,\quad
 \nu_j=(-1)^jq^{j(j+1)},\qquad F_j=\nu_jP_j.
\tag{1}
\]
All displayed factorial indices are below \(N\). Write
\[
 X=e^{-2\pi ia},\quad Y=e^{2\pi iy},\quad
 p_j(Z)=(rZ;r)_j,\quad
 \tau_m(Z)=\prod_{h=m+1}^{D}(1-Zr^h).
\tag{2}
\]
The original Fourier basis and cap are
\[
 f_m(y)=\frac{e^{-\pi iDy}}N\,Y^m\tau_m(Y),
 \qquad
 Z_N(a,y)=\sum_{l=0}^{D}C_{1,N}(X,r^l)f_l(y),
\tag{3}
\]
where
\[
 C_{\epsilon,N}(X,W)
   =\sum_{j=0}^{D}
      \frac{X^{-j}p_j(X)p_j(W)}{P_j^{2+\epsilon}}.
\tag{4}
\]
These are the literal sources of
[exact wire contraction](research_mixed_wire_exact_contraction.md)
and [conditional composition](research_mixed_conditional_torus_composition.md).
In particular \(f_m\) includes its \(1/N\); no additional crossing
scalar is included in \(Z_N\).

Let \(\mathcal M_n\) act by the original signed crossing matrix,
as in [the closing interface](research_mixed_fourier_boundary_closing_interface.md):
if \(G=c^Tf\), then
\[
       \mathcal M_nG=c^TSM^nS^{-1}f,\qquad
 S=D_0M,\quad (D_0)_{mm}
       =\frac{\kappa^{-1}(-q)^{-m}}{P_m}.
\tag{5}
\]
Write \(c_m^{(n)}(X)\) for every coefficient of
\(\mathcal M_nZ_N\), rather than only \(c_0^{(n)}\).
The physical-input identity in
[the signed dictionary](research_mixed_fourier_signed_crossing_coefficients.md),
equation (17), identifies the entire row
\[
 c(X)^TS\big|_{X=r^b}
       =\frac{(-q)^{-b}}{\kappa^2N}\,
                        \mathbf e_b^TM^*M^3.
\]
Consequently
\[
 \boxed{\quad
 c_m^{(n)}(r^b)
    =\frac{(-q)^{m-b}P_m}{\kappa N}
                         (M^*M^{n+2})_{bm},
       \qquad 0\le b,m<N .
 \quad}
\tag{6}
\]
Here \(M^*\) is the original conjugate transpose at the fixed
root of unity. It is not conjugation of either free boundary
parameter. To prove (6), substitute \(S^{-1}=M^{-1}D_0^{-1}\)
in (5). Both sides determine the unique incoming Laurent polynomial
of band \([-D,0]\). Thus interpolation of (6) keeps the entire
original source; it is not replacement by a different off-grid
representative.

## 2. One negative crossing: the complete weighted \(C_0\) transform

**Proposition 1.** For every \(X\ne0\) and every complex \(y\),
\[
 \boxed{\begin{split}
 \mathcal M_{-1}Z_N(a,y)
   &=\frac1{\kappa N}
        \sum_{m=0}^{D}P_mC_{0,N}(X,r^m)f_m(y)\\
   &=\frac1{\kappa N}
        \sum_{\substack{j,m\ge0\\j+m<N}}
          \frac{X^{-j}p_j(X)P_{j+m}}{P_j^2}\,f_m(y).
 \end{split}}
\tag{7}
\]
The whole triangular wall, every output mode, and the chirp in
\(f_m\) remain in (7).

*Proof.* The exact ordinary terminal polynomials of
[reversed-cap assembly](research_mixed_reversed_cap_assembly.md),
equation (10), have the coefficient forms
\[
 \mathcal V_{0,N}(w,X)
     =\sum_m P_mC_{0,N}(X,r^m)(Sv(w))_m,
 \qquad
 \mathcal V_{1,N}(w,X)
     =\sum_m C_{1,N}(X,r^m)(Sv(w))_m.
\tag{8}
\]
The factor \(P_m\) in the first line is necessary:
the original \(\mathcal H_N(w,r^{-m})\) equals
\(P_m(Sv(w))_m\).

The full ordinary-color identity in
[terminal color transport](research_mixed_terminal_color_transform.md),
equation (3), says that the coefficient row of \(\mathcal V_1\)
is the coefficient row of \(\mathcal V_0\), multiplied on the right
by \(M/(\kappa N)\). Apply \(M^{-1}\), and then the exact Fourier
change of basis \(S^{-1}f\). This proves the first line of (7).
At a physical second argument,
\[
 p_j(r^m)=
 \begin{cases}
 P_{j+m}/P_m,&j+m<N,\\
 0,&j+m\ge N.
 \end{cases}
\]
Substituting into (4) proves the second line. \(\square\)

Equivalently, (7) is \((\kappa N)^{-1}
\mathcal E_0[C_{0,N}(X,\cdot)]\), for the whole finite
intertwiner \(\mathcal E_0\) of
[the conditional/Fourier bridge](research_mixed_conditional_fourier_message_bridge.md),
equation (3). This is the Fourier version of the previously proved
ordinary-color transport, rather than a new type-three binomial
identity.

## 3. Two negative crossings: every coefficient in closed form

**Proposition 2.** The full coefficient row after two negative
crossings is
\[
 \boxed{\begin{split}
 c_m^{(-2)}(X)
  &=\frac{\kappa^{-2}P_m}{N^2}
      \sum_{k=0}^{D-m}\frac{P_{k+m}}{P_k}X^{-k}\\
  &=\frac{\kappa^{-2}P_m^2}{N^2}\tau_m(X^{-1}).
 \end{split}}
\tag{9}
\]
In particular this is a finite identity through \(m=D\), with
the empty product \(\tau_D=1\).

*Proof.* The original crossing entry from exact wire contraction is
\[
 M_{mb}=\kappa(-1)^mq^{m+b^2}{m\brack b}_Q,\qquad b\le m.
\]
At \(n=-2\), (6) therefore gives
\[
 c_m^{(-2)}(r^b)=
 \begin{cases}
 \displaystyle
 \frac{\kappa^{-2}}N\,
       \nu_b^{-1}\frac{P_m^2}{P_bP_{m-b}},&b\le m,\\
 0,&b>m.
 \end{cases}
\tag{10}
\]
Indeed the signs and powers outside the Gaussian binomial are
\[
 (-q)^{m-b}(-1)^mq^{-m-b^2}
                  =(-1)^bq^{-b(b+1)}=\nu_b^{-1}.
\]
For a Laurent polynomial \(\sum_{k=0}^{D}a_kX^{-k}\),
the coefficient is \(a_k=N^{-1}\sum_b c_m^{(-2)}(r^b)r^{bk}\).
The finite \(r\)-binomial identity now yields
\[
 \begin{split}
 \sum_{b=0}^{m}\nu_b^{-1}{m\brack b}_r r^{bk}
 &=\sum_{b=0}^{m}(-1)^b r^{b(b-1)/2}
                  {m\brack b}_r(r^{k+1})^b\\
 &=(r^{k+1};r)_m.
 \end{split}
\tag{11}
\]
For \(k+m<N\) this is \(P_{k+m}/P_k\); for
\(k+m\ge N\) it is zero. This proves the first line of (9).

For completeness, the finite polynomial identity giving the second
line is
\[
 \tau_m(z)=\sum_{k=0}^{D-m}
                  \frac{P_{k+m}}{P_mP_k}z^k.
\tag{12}
\]
To check it without an infinite series or a singular specialization,
the coefficient of \(z^k\) in its product is
\[
 (-1)^k r^{(m+1)k+k(k-1)/2}{D-m\brack k}_r.
 \]
The root complement gives
\[
 {D-m\brack k}_r
   =(-1)^kr^{-mk-k(k+1)/2}
                      \frac{P_{m+k}}{P_mP_k}.
\]
The powers and signs cancel exactly. Every denominator has index
below \(N\), including at both endpoints. This proves (12) and
(9). \(\square\)

Thus an intermediate one-index expression for the whole crossed
function is already
\[
 \mathcal M_{-2}Z_N(a,y)
   =\frac{\kappa^{-2}e^{-\pi iDy}}{N^3}
       \sum_{m=0}^{D}P_m^2Y^m\tau_m(Y)\tau_m(X^{-1}).
\tag{13}
\]
It has no added state-sum dimension and no unobserved Fourier
coefficient.

## 4. Collapse to one original conditional polynomial

**Theorem 3.** For every level \(N\ge2\), every \(X\ne0\),
and every complex \(y\),
\[
 \boxed{\qquad
 \mathcal M_{-2}Z_N(a,y)
   =\frac{\kappa^{-2}e^{\pi i(N-1)y}}N\,
                C_{0,N}(X,Y^{-1}).
 \qquad}
\tag{14}
\]
The argument is \(Y^{-1}=e^{-2\pi iy}\); it is neither
\(Y\) nor the conjugate of \(Y\).

*Proof.* The finite reciprocal product has the exact phase
\[
 \tau_m(X^{-1})=\nu_mX^{m-D}p_{D-m}(X).
\tag{15}
\]
Indeed reverse the factors \(1-X^{-1}r^h\) using
\(r^{-h}=r^{N-h}\). The factor
\((-1)^{D-m}r^{[N(N-1)-m(m+1)]/2}\) is precisely
\(\nu_m\). No logarithm is taken in this step.
Moreover
\[
 \nu_mP_m^2=P_mF_m=|P_m|^2,\qquad
 |P_{D-k}|^2=\frac{N^2}{|P_k|^2}.
\tag{16}
\]
The latter follows from \(P_D=N\) and
\(P_D/P_{D-k}=F_k\). Setting \(m=D-k\) in (9) gives the
entire coefficient, not just its physical values,
\[
             c_{D-k}^{(-2)}(X)
                  =\kappa^{-2}
                      \frac{X^{-k}p_k(X)}{P_kF_k}.
\tag{17}
\]
The original output basis in that same order is
\[
 f_{D-k}(y)=\frac{e^{-\pi iDy}}N
                  Y^{D-k}(YQ;Q)_k,\qquad
 (YQ;Q)_k=\nu_kY^k(rY^{-1};r)_k.
\tag{18}
\]
Insert (17)--(18), and use \(F_k=\nu_kP_k\).
The resulting sum is exactly (4) with \(\epsilon=0\)
and \(W=Y^{-1}\), while
\(e^{-\pi iDy}Y^D=e^{\pi iDy}\). This proves (14).
\(\square\)

All steps are finite polynomial identities, so possible numerator
zeros are retained without division. At even levels the chirp in
(14) is antiperiodic, exactly as the original half-band; at odd
levels it is periodic. The output frequencies remain
\(-D/2,\ldots,D/2\). The full Newton matrix used in (6) contains
its original repeated-node normals. Nothing in (14) takes a
value-only quotient of that matrix.

As a consistency check, (17) at \(k=D\) gives
\(c_0^{(-2)}=\kappa^{-2}N^{-2}\sum_{j=0}^{D}X^{-j}\),
the already proved first coefficient. Formula (14) supplies all
the other channels as well.

## 5. The new source problem is a specific one-index conditional problem

On an original regular logarithmic chart, the phase of the literal
conditional source in (14), including its external chirp, is
\[
 \Phi_{-2}(v;a,y)=
    g(v+a)+g(v+y)-2g(v)-g(a)-g(y)
                       +2\pi iav+\pi iy.
\tag{19}
\]
Here \(g\) is the original continued factorial primitive.
For example, the usual factorial interpolant applies on any compact
chart where \(a,y,v,v+a,v+y\) stay in their regular strips.
If
\[
 \mathfrak a(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2}
\]
has the original square-root continuation, the literal summand of
(14) then has symbol
\[
 \kappa^{-2}N^{-2}
 \frac{e^{-\pi iy}\mathfrak a(v+a)\mathfrak a(v+y)}
      {\mathfrak a(a)\mathfrak a(y)\mathfrak a(v)^2}
            e^{N\Phi_{-2}(v;a,y)}(1+O(N^{-1})).
\tag{20}
\]
This fixes the action constant as well as the \(N\) power.
If a contributing nondegenerate one-index saddle and a strict
whole-source remainder are subsequently proved on such a chart,
the lattice density \(N\) and Gaussian power \(N^{-1/2}\)
give \(N^{-3/2}\), with the scalar \(\kappa^{-2}\) retained.
Those additional analytic assertions are not consequences of
the algebraic identity.

In particular the exponentiated stationary equation is exactly
\[
       (1-XU)(1-Y^{-1}U)=X(1-U)^2,\qquad
                    U=e^{-2\pi iv}.
\tag{21}
\]
Equivalently, for \(T=U^{-1}\),
\[
       Y(X-1)T^2+(1-XY)T+X(Y-1)=0.
\tag{22}
\]
No root at a vanishing denominator is admitted by (21), and
exponentiation alone does not determine the zero logarithmic lift.

For comparison, (7) has the original two-index phase
\[
 \Phi_{-1}(s,t;a,y)
     =g(s+a)+g(s+t)-2g(s)-g(a)
                                  +2\pi ias+\ell_t(y),
\tag{23}
\]
where \(\ell_t\) is the original cardinal phase. Its exponentiated
critical equations, with \(S=e^{-2\pi is}\) and
\(T=e^{-2\pi it}\), are
\[
 \begin{split}
 (1-XS)(1-ST)&=X(1-S)^2,\\
 Y(1-ST)&=1-YT .
 \end{split}
\tag{24}
\]
At a regular solution,
\[
 T=\frac{Y^{-1}-1}{1-S},\qquad
             (1-XS)(1-S/Y)=X(1-S)^3.
\tag{25}
\]
Thus the two full sources have explicit, different original phase
problems; neither is obtained by keeping the old cap phase fixed.

The presently proved
[canonical conditional packets](research_mixed_conditional_critical_images.md)
apply at correlated typed images, whose type-three internal leg
has real part greater than \(.267\). In (14) the second retained
parameter is \(y=x_0\), with real part between \(.18\) and
\(.19\) and positive height. It is outside those supplied
conditional-image domains and the ordinary plateau \(P\).
The whole ordinary-color type-three packet near \(-2\) likewise
does not estimate the Fourier transform (7).

Consequently (14) removes the full crossing operator and the
two-index cap sum from this particular twice-crossed problem,
and replaces them by one already defined finite conditional
source at explicitly specified parameters. A nonzero asymptotic
still requires its original critical branch and logarithmic lift,
the complete physical/alias/vertical/join comparison, and the
correct geometric action. The previously paid first-coefficient
projections do not supply these missing statements. No full
crossing stability, ordinary closing lower bound, or new knot
family is claimed here.
