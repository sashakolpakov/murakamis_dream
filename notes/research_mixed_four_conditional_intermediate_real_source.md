# The complete conditional source on the intervening real arc

Private written deduction, 10 November 2026. The original type-four
conditional polynomial on the real interval from \(7/10\) to \(7/8\)
is bounded by its original critical exponential and the two old
real-half-face cut rates. The proof moves only a prewall core.
Every later physical row, including the postwall middle, is retained
and estimated directly. The original two unweighted joins and all
six weighted cotangent currents are included.

This is a complete conditional ceiling. Multiplication by a complete
cap and comparison with the original attached affine action remain
separate requirements; no full-period or knot conclusion is made.

## 1. Source, parameters and statement

Retain the original finite source and notation
\[
 q_N=e^{-2\pi i/N},\quad P_j=(q_N;q_N)_j,\quad
 p_j(Z)=(q_NZ;q_N)_j,\qquad
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                 \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{1}
\]
The targets are
\[
 \frac7{10}\le a\le\frac78,\qquad b=z+id,\qquad
 \frac{11}{50}\le z\le\frac9{20},\quad
 -\frac{51}{500}\le d\le-\frac1{1000},\qquad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib}.
 \tag{2}
\]
Write \(\delta=1-a\), so \(1/8\le\delta\le3/10\).
In particular \(1/2<|Y|<1\).

Use the original primitive and phase
\[
 \begin{split}
 g'(w)&=\operatorname{Log}(1-e^{-2\pi iw}),\qquad 0<\Re w<1,\\
 Q(s;a,b)&=g(a+s)+g(b+s)-3g(s)-g(a)-g(b)+2\pi ias,\\
 s_*&=u_*+ih_*,\qquad Q_s(s_*;a,b)=0,\qquad
 \Theta(a,b)=Q(s_*;a,b).
 \end{split}
 \tag{3}
\]
The critical point is the original upper-root branch, with its zero
logarithmic lift. The
[fixed lower-cut theorem](research_mixed_four_unit_arc_fixed_lower_cut.md)
proves on (2)
\[
          \ell:=\frac2{25}<u_*<\delta,\qquad
                         \frac15<|e^{2\pi is_*}|<2.
 \tag{4}
\]
Its strict strip gaps are uniform on this compact parameter set.

Let \(J\) be the original real sine primitive with its continuous odd
periodic extension, and put
\[
 \begin{split}
 I_x(t)&=\int_0^t\log|1-e^{-2\pi i(x+v)}|\,dv,\\
 I_b(t)&=\int_0^t\log|1-Ye^{-2\pi iv}|\,dv,\\
 E_x(t;b)&=I_x(t)+I_b(t)-3J(t),\qquad 0\le t\le1,\\
 L(b)&=E_{1/2}(\ell;b),\qquad H(b)=E_{1/2}(1/2;b).
 \end{split}
 \tag{5}
\]
These are continuous rates, including their integrable zeros and
endpoint limits. They are not moduli of finite cut rows.

**Theorem 1.** For every \(\tau>0\), there are \(C_\tau,A_\tau\)
such that, at both parities, uniformly on (2),
\[
 \boxed{\quad
 |C_{1,N}(X,Y)|\le C_\tau N^{A_\tau}
       \exp N\{\max(\Re\Theta(a,b),L(b),H(b))+\tau\}.
 \quad}
 \tag{6}
\]
Every original index \(0\le j<N\) occurs in the proof.
The main integral has its original \(+N\) coefficient and all
cotangent corrections their original \(N/(2i)\) coefficient.
No cap, Fourier polynomial, selected monomial or outgoing halfweight
has been divided out or replaced by this theorem.

## 2. The critical height and a whole prewall curvature strip

Put \(U=e^{2\pi h_*}=|e^{2\pi is_*}|^{-1}\).
Equation (4) already gives \(U>1/2\). In fact
\[
                   U<3,\qquad
        |h_*|<H_0:=\frac{\log3}{2\pi}.
 \tag{7}
\]
To prove the new upper bound, suppose \(U\ge3\).
For \(R>1\) and \(0<V<2\pi\), the original argument has the identity
\[
 \alpha_R(V):=\Arg(1-Re^{-iV})
       =\pi-V+\Arg(1-R^{-1}e^{iV}),\qquad
 |\Arg(1-R^{-1}e^{iV})|\le\arcsin(R^{-1}).
 \tag{8}
\]
Apply it to the incoming, outgoing and own logarithms in (3).
The outgoing radius is \(|Y|U>3/2\).
Writing \(u=u_*\), the leading arguments sum exactly to
\(-\pi-2\pi z+2\pi u\). Their total upper error is at most
\[
             4\arcsin(1/3)+\arcsin(2/3)<\frac{3\pi}{4}.
 \tag{9}
\]
Indeed \(\sin(\pi/8)>1/3\) and \(\sin(\pi/4)>2/3\), as follows
by squaring their original positive elementary values.
Since \(u<\delta\le3/10\) and \(z\ge11/50\), (8)--(9) yield
\[
             \Im Q_s<-\frac{21\pi}{25}+\frac{3\pi}{4}
                         =-\frac{9\pi}{100}<0.
 \tag{10}
\]
This contradicts the original zero lift. Thus \(U<3\).
Together with \(U>1/2\), it proves (7).

Define
\[
 \mathcal C(w)=\Re\cot(\pi w)
   =\frac{\sin(2\pi\Re w)}
          {\cosh(2\pi\Im w)-\cos(2\pi\Re w)}.
 \tag{11}
\]
On the entire prewall rectangle
\[
            \ell\le u\le\delta,\qquad |\sigma|\le H_0,
 \tag{12}
\]
with the wall interpreted only by its one-sided limit when needed,
\[
               -\Re Q_{ss}(u+i\sigma;a,b)>\frac{3\pi}{140}.
 \tag{13}
\]
All actual contours below stop strictly before the wall.

Here is a written verification. The incoming cotangent has negative
real part, since \(1/2<a+u<1\).
If \(\mathcal C(b+s)>0\), then \(z+u<1/2\), hence \(u<7/25\).
On \(\ell\le u\le7/25\),
\[
 \sin(2\pi u)>\frac{12}{25},\qquad
 \cos(2\pi u)>-\frac15,\qquad
 \cosh(2\pi\sigma)\le\cosh(\log3)=\frac53.
 \tag{14}
\]
For the first sine bound its smaller endpoint is \(4\pi/25\).
Using \(157/50<\pi<22/7\) and \(4\pi/25<101/200\),
\[
 \sin(4\pi/25)>
       \frac{314}{625}-\frac{(101/200)^3}{6}>\frac{12}{25};
 \tag{15}
\]
the last comparison is \(672000000>643938125\).
At the other endpoint,
\(\sin(14\pi/25)=\cos(3\pi/50)>49/50\).
The cosine assertion in (14) follows from
\(\sin(3\pi/50)<1/5\).
Consequently
\[
 \mathcal C(s)>\frac{9}{35},\qquad
 \mathcal C(b+s)\le\cot(3\pi/10)<\frac34.
 \tag{16}
\]
For the last bound, \(\cot(3\pi/10)=\tan(\pi/5)\), and
\(\tan^2(\pi/5)=5-2\sqrt5<9/16\); squaring
\(71/32<\sqrt5\) verifies it.
If instead \(\mathcal C(b+s)\le0\), then on the slightly longer
interval \(u\le3/10\) one has \(\sin(2\pi u)>12/25\) and
\(\cos(2\pi u)>-1/3\), so \(\mathcal C(s)>6/25\).
Finally, the exact Hessian identity is
\[
 -\Re Q_{ss}
   =\pi\{3\mathcal C(s)-\mathcal C(a+s)-\mathcal C(b+s)\}.
 \tag{17}
\]
In the first case its lower bound is
\(\pi(27/35-3/4)=3\pi/140\); the second gives a larger positive
bound. This proves (13). Thus horizontal restrictions are strictly
concave, while vertical restrictions are strictly convex.

## 3. The physical rows outside a prewall core

The rate comparisons used here are valid for every real
\(1/2\le x\le1\), not just the targets in (2):
\[
 E_x(t;b)\le E_{1/2}(t;b)\quad(0\le t\le1/2),\qquad
 E_x(t;b)\le H(b)\quad(1/2\le t\le1).
 \tag{18}
\]
For completeness, these are the exact rate arguments in Section 4 of
[the far-right physical theorem](research_mixed_initial44_far_right_physical_envelope.md).
At fixed \(t\le1/2\), the derivative of \(I_x(t)\) is
\(\log|\sin\pi(x+t)/\sin\pi x|\). Its sign changes only from
negative to positive, at \(x=1-t/2\); its numerator zero is handled
by integration. Its maximum on \([1/2,1]\) is therefore at an endpoint.
Those values are \(I_{1/2}(t)=-J(1/2-t)\ge0\) and
\(I_1(t)=J(t)\le0\), proving the first assertion.

For the second put \(v=1-t\), \(\delta=1-x\), and
\(G_{-d}(r)=\Re g(r+id)\). Exact reflection gives
\[
 E_x(1-v;b)
 =J(\delta)-J(\delta+v)
       +G_{-d}(z-v)-G_{-d}(z)+3J(v).
 \tag{19}
\]
The legwise inequality of
[the all-angle theorem, Lemma 1](research_mixed_all_angle_high_row_sign_class.md)
gives
\[
 G_{-d}(z-v)+J(v)+G_{-d}(1/2-z)\le0 .
 \tag{20}
\]
Also \(J(\delta)+2J(v)-J(\delta+v)\le0\).
If \(\delta+v\le1/2\), this follows from the increasing derivative
of \(J\) there and \(J(v)\le0\). Otherwise \(J(\delta),J(v)\le0\)
and \(J(\delta+v)\ge0\). Inserting these inequalities in (19)
gives exactly \(H(b)=-G_{-d}(z)-G_{-d}(1/2-z)\), proving (18).
Only the outgoing leg of (20) uses an angle below one half.

The first comparison in (18) also bounds every low row by \(L(b)\).
Indeed \(E_{1/2}(t;b)\) increases on \(0<t\le\ell\):
\[
 e^{E'_{1/2}(t;b)}
  =\frac{2\cos(\pi t)\,|1-Ye^{-2\pi it}|}
               {(2\sin\pi t)^3}>1.
 \tag{21}
\]
Here \(2\cos\pi t>3/2\), \(2\sin\pi t<3/5\), and
\(|1-Ye^{-2\pi it}|>4/5\). The last inequality follows from
\(\cos(2\pi(z+t))<1/5\) and the squared lower bound \(24/25\).
Thus the ratio in (21) exceeds \(50/9\).

For every postwall middle row, \(\delta\le t\le1/2\),
\[
 I_x(t)=J(\delta)+J(t-\delta)\le J(t),\qquad
                         E_x(t;b)\le E_1(t;b).
 \tag{22}
\]
The sine-binomial entropy inequality here follows by integrating
the increasing derivative \(J'\) on \((0,1/2)\).
Equation (13) of
[the near-endpoint complete-pair proof](research_mixed_initial44_near_endpoint_complete_pair.md)
proves the stronger, outgoing-correlated comparison
\[
           E_1(t;b)=I_b(t)-2J(t)
                      <L(b)-\frac2{375},
                 \qquad \ell\le t\le1/2.
 \tag{23}
\]
Only that equation's \(x=1\) rate inequality is used; it depends on
\(b,t\), not on the later \(x\ge7/8\) scope of its finite-pair
application. In particular the actual moving-wall rate is exactly
\[
                         E_x(\delta;b)=E_1(\delta;b).
 \tag{24}
\]
Thus it has the strict reserve in (23).

By compactness, choose a single sufficiently small \(\eta>0\) such that
\[
 \ell<u_*<r(a):=\delta-\eta<\delta,\qquad
 E_x(t;b)<L(b)-\frac1{375}
                 \quad(\delta-\eta\le t\le\delta)
 \tag{25}
\]
uniformly on (2). The first condition uses (4), and the second uses
(24) and uniform continuity of the integrated rates.
This choice is fixed before \(N\) and before any requested final
rate tolerance. Consequently every row outside the core
\([\ell,r(a)]\) is bounded by \(L(b)\) or \(H(b)\), with the stronger
strict margin in (25) on its short prewall collar.

These continuous statements give literal finite-row bounds, including
zeros and \(j=0,N-1\), by the regularized-log product proof in
Section 3 of the all-angle theorem. Its denominator estimate is
\(\log|P_j|=NJ(j/N)+O(\log N)\) uniformly at both ends; the numerator
upper errors tend uniformly to zero after regularization.
No row is replaced by a finite half-row value.

## 4. All alias sides on a fixed tall rectangle

Write \(R(u,\sigma)=\Re Q(u+i\sigma;a,b)\) on the whole prewall
strip \(\ell\le u\le r(a)\). Every factorial argument has real
part in a fixed compact subset of \((0,1)\), even when
\(|\sigma|\) is larger than \(H_0\). On all heights,
\[
 \begin{aligned}
 R_\sigma&\le\frac{87\pi}{50}&&(\sigma\ge0),\\
 R_\sigma&\ge-\frac{39\pi}{20}&&(\sigma\le0).
 \end{aligned}
 \tag{26}
\]
These are estimates of the original phase, including its chirp.
To check them, put
\(\mathcal A(w)=\Arg(1-e^{-2\pi iw})\). Exact differentiation gives
\[
 R_\sigma=-\mathcal A(a+s)-\mathcal A(b+s)
                              +3\mathcal A(s)-2\pi a .
 \tag{27}
\]
For \(\sigma\ge0\), use
\[
 \mathcal A(a+s)\ge\pi-2\pi(a+u),\qquad
 \mathcal A(s)\le\pi-2\pi u,\qquad
 \mathcal A(b+s)\ge\min(0,\pi-2\pi(z+u)).
 \tag{28}
\]
The first two use the incoming and own radius at least one;
the last is valid for every positive outgoing radius.
They yield
\[
 R_\sigma\le
 2\pi-4\pi u+\max(2\pi(z+u)-\pi,0)\le87\pi/50.
 \tag{29}
\]
In the first alternative the ceiling is \(42\pi/25\);
in the second it is
\(\pi+2\pi z-2\pi u\le87\pi/50\).

For \(\sigma\le0\), the incoming argument is nonpositive and
the own argument nonnegative. The outgoing radius is below one.
If \(z+u<1/2\), its argument is at most
\(\pi/2-\pi(z+u)\le\pi/5\); otherwise it is nonpositive.
Since \(a\le7/8\), (27) gives the lower bound in (26).

It follows that both weighted vertical rates decrease away from
their real cuts:
\[
 \begin{aligned}
 \partial_\sigma(R-2\pi\sigma)&\le-13\pi/50&&(\sigma\ge0),\\
 \partial_\sigma(R+2\pi\sigma)&\ge\pi/20&&(\sigma\le0).
 \end{aligned}
 \tag{30}
\]
The same inequalities integrated to height \(\pm T\) give an arbitrary
fixed loss on both horizontal aliases when \(T\) is chosen large
enough. More explicitly, let \(M\) bound \(R(u,0)\) above on the
closed parameter/core family, and let \(m\) bound \(\Re\Theta\) below.
Both are finite. Choose, before \(N\),
\[
                 T>H_0+1,\qquad
                 \frac{\pi T}{20}>M-m+1.
 \tag{31}
\]
Both horizontal weighted rates are then less than
\(\Re\Theta-1\). No imaginary direction is taken to infinity.
The unweighted joins below use only \(|\sigma|\le H_0\), where the
separate curvature proof applies.

## 5. Exact finite assembly

The original negative-root interpolant is
\[
 \begin{split}
 \Pi_N(w)&=G_N(Nw)
        \exp\!\left\{\frac{\pi i}{2}[N(w-w^2)-w]\right\},\qquad
 E_N(w)=1/\Pi_N(w)\quad(0<\Re w<1),\\
 T_N(s;a,b)&=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(b+s)
                                  E_N(a)E_N(b)E_N(s)^3 .
 \end{split}
 \tag{32}
\]
These are exactly the functions in
[the joint global chart, equations (2), (4), (6)](research_mixed_fourier_right_cap_joint_global_chart.md)
and [the original middle reduction, equation (3)](research_mixed_conditional_lower_output_middle_reduction.md).
At every integer \(j\) in the core, \(T_N(j/N)\) is the summand of
(1). The [canonical factorial expansion](exact_factorial_interpolation_and_complex_contours.md),
Section 4, gives its uniform polynomial-times-\(e^{NR}\) upper bound
on the full fixed rectangle \(|\Im s|\le T\).
All arguments remain in regular compact strips; no numerator
period factor is removed on this prewall core.

Choose the exact half-grid cuts
\[
 \begin{aligned}
 L_N&=\lfloor N\ell\rfloor+1,&
 M_N&=\lceil Nr(a)\rceil,\\
 \ell_N&=(L_N-\tfrac12)/N,&
 r_N&=(M_N-\tfrac12)/N .
 \end{aligned}
 \tag{33}
\]
For sufficiently large \(N\), they still enclose \(s_*\) in real
part and remain prewall with all strict strip margins.
The exact decomposition is
\[
 \begin{split}
 C_{1,N}(X,Y)
  &=C^{\rm low}_N+
        N\int_{\ell_N}^{r_N}T_N(s)\,ds+
        \mathcal R_N+C^{\rm later}_N,\\
 C^{\rm low}_N&=\sum_{0\le j<L_N}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\qquad
 C^{\rm later}_N=\sum_{M_N\le j<N}
                              \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
 \mathcal R_N&=\frac{N}{2i}\left\{
    \int_{\partial R^+_{\rm off}}T_N(\cot\pi Ns+i)\,ds+
    \int_{\partial R^-_{\rm off}}T_N(\cot\pi Ns-i)\,ds\right\}.
 \end{split}
 \tag{34}
\]
The two off-real boundaries have their original induced orientations;
the six pieces are the two horizontals at \(\pm T\) and four
vertical halves. Equation (34) is the original split-cotangent
identity, equation (15) of the middle reduction, with new cuts.

Its unweighted integral is moved exactly to the actual critical height:
\[
 \int_{\ell_N}^{r_N}T_N(s)\,ds
 =\int_{\ell_N}^{\ell_N+ih_*}T_N(s)\,ds
  +\int_{\ell_N+ih_*}^{r_N+ih_*}T_N(s)\,ds
  +\int_{r_N+ih_*}^{r_N}T_N(s)\,ds .
 \tag{35}
\]
The original zero lift and (13) put the unique horizontal maximum
at \(s_*\), with rate \(\Re\Theta\). Vertical convexity on the
short joins bounds each by the larger endpoint rate:
\(\Re\Theta\) or the corresponding real-cut rate.
The latter tends to \(E_a(\ell;b)\le L(b)\) on the left and
to \(E_a(r(a);b)<L(b)-1/375\) on the right.

On the exact half-grid sides,
\[
 |\cot(\pi Ns)\pm i|\le2e^{-2\pi N|\Im s|}
 \tag{36}
\]
with the matching upper or lower sign.
Thus (30) controls the whole four vertical half-currents by
their real-cut rates. On the horizontal sides the same bound
has factor four for all sufficiently large \(N\); (31) gives their
strict critical-rate loss. No denominator in a sampling kernel
is omitted.

The strict curvature and slope bounds persist on a small fixed
real enlargement of the cuts. Their \(O(1/N)\) displacements,
the continuous-rate collar bounds, and the original zero-safe
physical estimates can therefore all be absorbed into any prescribed
total tolerance. Section 3 bounds \(C^{\rm low}_N\) by \(L(b)\)
and \(C^{\rm later}_N\) by \(\max(L(b),H(b))\), retaining every
true endpoint and every postwall index.
Equations (34)--(36) now prove (6), with the original measures
and at most polynomial costs. This is independent of parity.

## 6. What this establishes and what remains separate

The theorem controls the entire original conditional polynomial,
including the interval that an endpoint shrinking-core argument leaves
as an extra physical middle block. It does so by using a fixed lower
cut, a fixed offset before the moving incoming wall, and the exact
postwall entropy comparison. No claim that a postwall critical-height
force stays below one is used.

To bound the actual first pair, one must still control its literal
\(U_{1,N}(w,X)\), multiply the whole \(d_N(X)X^{-N\sigma}\) and
the outgoing \(|d_N(Y)|^{1/2}\), and compare all three alternatives
in (6) with the unchanged affine action. In particular the theorem
does not equate \(|C_{1,N}|\) to its critical exponential or infer a
nonzero coefficient. It has no assertion about later-coordinate
selections, full-period composition or knots.

## Frozen source bindings

| Direct source | SHA-256 |
|---|---|
| research_mixed_four_unit_arc_fixed_lower_cut.md | a2e6a56f0ff12705e6c2b7a738122ed5bd98d095cfef6bb7a593a864b2c06293 |
| research_mixed_initial44_far_right_physical_envelope.md | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_initial44_near_endpoint_complete_pair.md | 4a481d134c93b8bb11bed2406253cec046f6e04a95339b1b48a8594469bc7712 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| research_mixed_conditional_lower_output_middle_reduction.md | 9df0e7cdf4a193783e236e8e0fa8f416b5a123d8afe02033601be333cf6d5bc7 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
