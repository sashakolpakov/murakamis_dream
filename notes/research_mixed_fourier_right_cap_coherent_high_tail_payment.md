# Payment of the entire coherently contracted high-index tail

Research deduction, 7 November 2026. The outgoing saddle at retained
index \(s=1/2\) lies in the old real target interval. Its action is
a vertical minimum on that line, so the proved inner half-row
comparison pays the coherently summed half-index face. The analytic
Wall rate reduction then pays every remaining high retained index.

This is an estimate for the actual part of the original finite
source with \(j\ge\lceil N/2\rceil\), after its outgoing index is
summed exactly. It does not assert that the other retained-index
currents have been controlled, or prove a whole-cap lower bound.
No root, analytic function, or new rate is evaluated.

## 1. The half-index outgoing saddle is an admitted target

Keep the original \(Y=e^{2\pi ix_0}\), and put
\[
 c=Y^{-1}-1=a_0-ib_0,\qquad
 -\frac7{20}<a_0<-\frac{37}{121},\qquad
 \frac{60}{41}<b_0<\frac{61}{40}.
 \tag{1}
\]
These are the inherited analytic bounds in the
[high-index branch theorem](research_mixed_fourier_right_cap_wall_high_index_branch.md).
At its endpoint \(t=1/2\), the original outgoing root satisfies
\[
 Q^2-(3+c)Q+c=0,\qquad |Q|<1,\qquad
 Q=e^{-2\pi iq_c},\quad 0<\Re q_c<1/2,\quad \Im q_c<0.
 \tag{2}
\]
All these branches and logarithmic lifts have already been proved.
The following argument sharpens only the real coordinate.

**Lemma 1.**
\[
                     \frac{11}{50}<\Re q_c<\frac38.
 \tag{3}
\]

*Proof.* Write \(Q=u-iv\), with \(v>0\), and let \(d=3+a_0\).
The imaginary part of (2) gives
\[
                  v=\frac{b_0(1-u)}{d-2u}.
 \tag{4}
\]
If \(u\le0\), the lower bound in (3) follows already from
\(\Re q_c\ge1/4\). Suppose therefore that \(u>0\).
Since \(|Q|<1\), one has \(0<u<1\), and \(d>53/20>2\).
Define the right side of (4) for every \(0\le u\le1\).
It satisfies
\[
 v'(u)=\frac{b_0(2-d)}{(d-2u)^2}<0,\qquad
                         0\le v(u)<b_0/2.
 \]
The real part of the quadratic is
\[
 f(u):=u^2-du+a_0+b_0v(u)-v(u)^2=0.
 \tag{5}
\]
On this interval,
\[
 f'(u)=2u-d+(b_0-2v(u))v'(u)<0.
 \tag{6}
\]

At \(u=1/10\), write \(r=v(1/10)/b_0\). Then
\[
 0<r=\frac{9/10}{d-1/5}<\frac{18}{49}<\frac25,
 \qquad b_0^2<\left(\frac{61}{40}\right)^2<\frac73.
 \]
The function \(r(1-r)\) increases up to \(r=1/2\), so
\[
 b_0v(1/10)-v(1/10)^2
       =b_0^2r(1-r)<\frac73\frac6{25}=\frac{14}{25}.
 \]
Consequently
\[
 f(1/10)<\frac{27}{100}+\frac9{10}a_0
        <\frac{27}{100}-\frac{333}{1210}
        =-\frac{63}{12100}<0.
 \tag{7}
\]
Strict decrease in (6) excludes a zero at or above \(1/10\);
hence the actual root has \(u<1/10\). Equation (4) now gives
\[
 v>v(1/10)>
       \frac{(60/41)(9/10)}{326/121-1/5}
       =\frac{32670}{61869}>\frac{21}{40}.
 \tag{8}
\]
The last comparison has positive cross-product difference \(7551\).
Thus \(u/v<4/21\).

The elementary inequality \(\tan z>z+z^3/3\) for \(0<z<\pi/2\)
follows by integrating \((\tan z)'=1+\tan^2z\) and \(\tan z>z\).
The elementary lower bound \(\pi>157/50\) follows, for example,
from Machin's identity and the alternating arctangent series:
\(\pi>16(1/5-1/375)-4/239>157/50\). Consequently
\[
 \tan(3\pi/50)>
 \frac{471}{2500}+\frac13\left(\frac{471}{2500}\right)^3
                                      >\frac4{21}.
 \tag{9}
\]
For the last rational inequality one may use
\(21\cdot471^3>327\cdot2500^2\).
Therefore
\[
 -\arg Q=\frac\pi2-\arctan(u/v)>\frac{11\pi}{25},
 \]
proving \(\Re q_c>11/50\).

For the upper bound, use the exact identity
\[
                         Q=\frac{c}{3+c-Q}.
 \tag{10}
\]
The denominator has positive real part, since
\(3+a_0-u>33/20\), and negative imaginary part, since
\(-b_0+v<0\). Also \(b_0>-a_0>0\), so
\(-3\pi/4<\arg c<-\pi/2\). The difference of these two
arguments belongs to \((-3\pi/4,0)\); hence it is the
original lower-half-disk argument of \(Q\). It follows that
\(\Re q_c<3/8\). This proves (3). \(\square\)

In particular \(z_c=\Re q_c\) belongs to
\(P=[11/50,9/20]\), with a strict margin.

## 2. The outgoing action is a vertical minimum at this saddle

Define the original outgoing action at retained index \(1/2\) by
\[
 K(q)=g(1/2+q)-g(q)+\ell_q(y),\qquad y=x_0.
 \tag{11}
\]
The original high-index branch has \(K'(q_c)=0\), not merely
the corresponding exponentiated equation.

**Lemma 2.** For every \(h\le0\),
\[
                         \Re K(q_c)\le\Re K(z_c+ih).
 \tag{12}
\]

*Proof.* On the whole line \(q=z_c+ih\), \(h\le0\), both
factorial arguments have real parts strictly between zero and one.
Since \(0<z_c<1/2\),
\[
 \Re\cot\pi q>0,\qquad
 \Re\cot\pi(1/2+q)<0.
 \]
Also the inherited Fourier angle obeys \(8/7<\phi<7/6\).
Lemma 1 implies
\[
              -\pi<\phi-2\pi z_c<0.
 \]
For \(Z=Ye^{-2\pi iq}\), one has \(|Z|\le|Y|<1\) and
\[
 \Re\ell''_q(y)=\frac{2\pi\Im Z}{|1-Z|^2}<0.
 \]
Using the original identity \(\Re g''(w)=\pi\Re\cot\pi w\),
all three terms give
\[
                       \Re K''(z_c+ih)<0
                                            \qquad(h\le0).
 \tag{13}
\]
Therefore \(h\mapsto\Re K(z_c+ih)\) is strictly convex.
At \(h=\Im q_c<0\), its derivative is
\(-\Im K'(q_c)=0\). This proves the global minimum (12) on
the negative vertical half-line. No finite source is reset in
height by this comparison; it compares two values of the
already calibrated outgoing critical action. \(\square\)

## 3. The old half-row bound pays the coherent half-index face

Retain the actual source family and allocation of the
[completed bare inner-source theorem](research_mixed_fourier_right_cap_bare_inner_completion.md):
\[
 \eta\in\{0,1\},\quad a_*\in K_{3+\eta},\quad
 (s_*,q_*)\in O_4^2,\qquad
 a=x+i\Im a_*,\quad x\in P.
 \tag{14}
\]
Put \(h_*=\Im q_*<0\), and keep exactly its original supporting
plane
\[
 \begin{split}
 B_\eta(x)&=M_\eta+p_\eta(x-\Re a_*)
                            -\kappa(x-\Re a_*)^2,\\
 \mathcal L_\eta(x,z)&=B_\eta(x)-\kappa(z-\Re q_*)^2,
                   \qquad \kappa=1/2500000.
 \end{split}
 \tag{15}
\]
The proved half-row comparison from that theorem is
\[
 \mathcal T_\eta(1/2;x,z)
              <\mathcal L_\eta(x,z)-\frac1{35000},
                                      \qquad x,z\in P.
 \tag{16}
\]
This is an individual original profile bound; it is not inferred
from a modulus bound on a canceled sum.

Let \(\mathcal E_\eta\) be the zero-safe coherent retained rate
in the
[retained-rate theorem](research_mixed_fourier_right_cap_coherent_retained_rate.md).
At \(s=1/2\) there is no incoming wrap:
\(.72\le\Re(a+1/2)\le.95\), and the original regular strip gives
\[
 I_a(1/2)=\Re\{g(a+1/2)-g(a)\}.
 \]
Consequently, with the same action constant and chirp,
\[
 \begin{split}
 \mathcal E_\eta(1/2;a)
 =\Re\big\{&
   g(a+1/2)-(1+\eta/2)g(a)-3g(1/2)\\
   &+\pi ia+K(q_c)\big\}.
 \end{split}
 \tag{17}
\]
Here \(\Re g(1/2)=J(1/2)=0\), but its original complex
constant has been left displayed.
Apply (12) with \(h=h_*\). The right side of (17) is at most
the original row profile \(\mathcal T_\eta(1/2;x,z_c)\).
The two factorial real arguments involving \(z_c\) also lie in
their regular strips. Lemma 1 makes \(z_c\) an allowed target
of (16). Hence
\[
 \boxed{\quad
 \mathcal E_\eta(1/2;a)
   <\mathcal L_\eta(x,z_c)-\frac1{35000}
   \le B_\eta(x)-\frac1{35000}.
 \quad}
 \tag{18}
\]
The incoming complex marginal, full reference action, outgoing
zero marginal and both original allocations in (15)--(18) are
unchanged. No outgoing halfweight has been introduced or divided out.

## 4. The complete high-index finite-source consequence

The analytic
[Wall rate theorem](research_mixed_fourier_right_cap_wall_rate_convexity.md)
proves on the whole interval \(1/2\le s\le1\) that
\[
 \mathcal E_\eta(s;a)
       \le\max\{\mathcal E_\eta(1/2;a),\mathcal E_\eta(1;a)\}.
 \]
Its second endpoint is exactly the true physical endpoint.
The [endpoint-payment theorem](research_mixed_fourier_right_cap_endpoint_payment.md)
gives \(\mathcal E_\eta(1;a)<B_\eta(x)-387/70000\).
Together with (18), this proves the uniform rate bound
\[
             \mathcal E_\eta(s;a)
                  <B_\eta(x)-1/35000,\qquad 1/2\le s\le1.
 \tag{19}
\]

Keep the literal outgoing contraction
\[
 H_{j,N}(y)=
       \sum_{l=0}^{N-j-1}\frac{P_{j+l}}{P_l}f_l(y),
 \quad P_j=(r;r)_j,\quad r=e^{-2\pi i/N},\quad
 X=e^{-2\pi ia}.
 \tag{20}
\]
The completed half-degree asymptotic, the zero-safe incoming
product bound, and the overlapping exact endpoint strip now give,
for every prescribed \(\tau>0\), uniformly on the actual compact
families (14),
\[
 \boxed{\begin{split}
 &|d_N(X)|^{\eta/2}
 \left|\sum_{j=\lceil N/2\rceil}^{N-1}
       X^{-j}\frac{(rX;r)_j}{P_j^3}H_{j,N}(y)\right|\\
 &\qquad\le C_\tau N^{A_\tau}
       \exp N\{B_\eta(x)-1/35000+\tau\}.
 \end{split}}
 \tag{21}
\]
For sufficiently large levels, the finite exponential gap may
therefore be taken to be \(1/70000\). Both parities, the exact
degree shift \(N-j-1\), the cardinal factor \(1/N\), all original
outgoing physical rows and every zero of the incoming polynomial
are retained. Multiplication by the incoming halfweight is an
upper bound for its actual modulus, never division by a finite
value.

The fixed outgoing saddle and the strict strip and profile margins
also persist on a small output neighborhood of \(x_0\), with a
smaller common margin and the original continued reference data.
This does not give a whole outgoing-period assertion.

Equation (21) pays the entire high-index physical part after
coherent outgoing contraction. This decomposition first splits the
retained index \(j\), and keeps every outgoing row together within
each \(H_{j,N}\). It includes the old high-inner/low-outgoing wedge
inside that whole contraction, but does not bound that wedge
separately or justify inserting its bound termwise into the old
two-dimensional contour split. It does not by itself estimate the
low retained indices, their contour joins, or a complete right-cap remainder.
It proves no lower bound for the full right cap or an attached
knot invariant.
