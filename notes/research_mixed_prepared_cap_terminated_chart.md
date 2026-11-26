# A coherent terminating chart for the prepared three-four cap

Research deduction, 7 November 2026. The exact physical type-three
cap identity removes the private index whose artificial upper cut
failed in the first prepared-source comparison. Applied before any
interpolation, it gives a different four-index expression for the
whole original prepared source. Its regular contour box has a
strictly accretive phase and contains the already proved original
critical point. This is an exact source and curvature theorem, not
a new tail or alias comparison. No function has been evaluated.

## 1. The finite rearrangement comes first

Keep the notation of
[the original prepared source](research_mixed_prepared_three_four_cap_source.md):
\[
 \zeta=e^{\pi i/N},\quad r=\zeta^{-2},\quad Q=r^{-1},\quad
 P_j=(r;r)_j,\quad \kappa=\zeta^{(N-1)^2/2},\quad
 Y=e^{2\pi iy},\quad
 c_y=N^{-1}e^{-\pi i(N-1)y}(1-Y^N).
 \tag{1}
\]
The symbol \(e_a(w)\) below is the original complete Newton
polynomial, including its normal terms. All four summation indices
are distinct.

**Proposition 1.** At every level \(N\ge2\), the whole function
\(G_{34,N}(y,w)=v(w)^TA_3A_4h(y)\) equals
\[
 \boxed{\quad
 \kappa^3N^2c_y
 \sum_{\substack{a,j,k,l\ge0\\a+j<N,\ j+k<N,\ k+l<N}}
 \frac{(-\zeta)^{-a}e_a(w)\,Y^lQ^{jk}
       P_{a+j}P_{j+k}P_{k+l}}
      {P_a^2P_j^3P_k^3P_l(Y;r)_{l+1}} .
 \quad}
 \tag{2}
\]
The same identity holds after any fixed ordinary-color derivative.
It retains both level parities.

*Proof.* Equation (5) of the prepared-source theorem is the exact
three-index sum with coefficient
\(U_{0,N}(w,r^j)/P_j\). Lemma 1 of
[the physical type-three cap theorem](research_mixed_three_first_cap_packet.md)
is the all-level finite identity
\[
 U_{0,N}(w,r^j)
 =\frac{N}{P_j^2}
       \sum_{a=0}^{N-1-j}
          (-\zeta)^{-a}e_a(w)\frac{P_{j+a}}{P_a^2}.
 \tag{3}
\]
Insert (3) into that finite sum and interchange finite summations.
Its factor \(N/P_j^2\) changes the outside scalar from
\(\kappa^3Nc_y\) to \(\kappa^3N^2c_y\), and the old
\(P_j\) in the denominator becomes \(P_j^3\).
The new support \(a+j<N\) is exactly the terminating support
in (3). The other two supports are unchanged. This proves (2).
\(\square\)

In particular (2) does not substitute a terminating off-grid
expression for \(U_{0,N}(w,X)\). The exact identity is proved
on the entire finite source first; its individual factorial rows
may then receive their own exact interpolation. The wrapped
Fourier replacement of \(U_0\) is neither invoked nor discarded.
There is no additional selection or Fourier weight in (2).

## 2. The original phase and its calibration

Write
\((u,t,p,q)=(a,j,k,l)/N\), and retain the original primitives
\[
 g(z)=J(z)+\frac{\pi i}{2}(z-z^2),\qquad J(0)=0,\qquad
 \ell_q(y)=2\pi iqy-I_Y(q)-\pi iy.
 \tag{4}
\]
Let
\[
 \begin{split}
 V_0(u)&=-2J(1/2-u)-2J(u),\\
 T(t,u)&=V_0(u)+g(u+t)-2g(u)-2g(t)+i\pi u,\\
 V(z,z')&=g(z+z')-g(z)-g(z').
 \end{split}
 \tag{5}
\]
The original positive lift \(+i\pi a\) of \((-1)^a\)
is the one used in the physical cap theorem. The phase of (2) is
\[
 \begin{split}
 \widetilde F(u,t,p,q;y,w=-2)
  ={}&T(t,u)+V(t,p)+V(p,q)-g(p)+2\pi itp+\ell_q(y)\\
  ={}&-2g(1/2-u)-4g(u)+g(u+t)+g(t+p)+g(p+q)\\
     &-3g(t)-3g(p)-g(q)
           +i\pi(1/4+2u-2u^2+2tp)+\ell_q(y).
 \end{split}
 \tag{6}
\]
The constant \(i\pi/4\), the positive Newton lift and the
chirp \(2\pi itp\) have all been retained.

**Proposition 2.** The original prepared critical point, with
its \(s\)-coordinate eliminated by its own original equation,
is a critical point of (6). Its critical value is exactly the
already calibrated prepared action, not just equal modulo a
constant.

*Proof.* Put \(R=e^{-2\pi iu}\), \(Z=e^{-2\pi it}\).
The original private \(s\)-equation gives
\[
 e^{-2\pi is}=\frac{R-1}{1-Z}.
 \tag{7}
\]
The physical cap theorem proves the exact identity
\[
 T(t,u)=F_0(t;s(u,t),u),
 \tag{8}
\]
where \(F_0\) is the original two-variable cap phase, first
on its real outgoing interval with the original lifts.
Here is a continuation argument that includes the present complex
critical point.

Use the connected product
\[
 .21<\Re u<.25,\quad .01<\Im u<.10,\qquad
 .278<\Re t<.391,\quad -.072<\Im t<.021 .
 \tag{9}
\]
On it define
\[
 s(u,t)=\frac14+\frac u2+
       \frac{\Log(1-Z)-\Log(2\sin\pi u)}{2\pi i}.
 \tag{10}
\]
Both logarithms have their indicated original branches.
Indeed \(0<\arg(1-Z)<\pi/3\): its real part is greater
than one, and its imaginary part is less than
\(e^{.042\pi}<6/5<\sqrt3\).
Also \(0<\arg\sin\pi u<\pi/6\), since
\[
 \tan(\arg\sin\pi u)
       =\cot(\pi\Re u)\tanh(\pi\Im u)
       <\frac{\Im u}{\Re u}<\frac{10}{21}<\frac1{\sqrt3}.
 \tag{11}
\]
Consequently (10) has
\[
 0<\Re(s-u)<\frac{187}{600}<\frac12,\qquad
 \frac12<\Re(s+t)<1 .
 \tag{12}
\]
For the first upper bound use
\(1/4-.21/2+1/6=187/600\).
The other bounds follow from
\(1/4-.25/2-1/12>0\),
\(1/4+.21/2+.278-1/12>1/2\), and
\(1/4+.25/2+.391+1/6<1\).
Thus all original sine strips in (8) remain regular.

Exponentiation of the original \(F_{0,s}\) gives one by (7).
Its imaginary part lies strictly between \(-2\pi\) and
\(2\pi\): the two logarithmic arguments have arguments in
\((-\pi,0)\) and \((0,\pi)\), respectively, and its chirp
adds \(2\pi\Re u\). Hence \(F_{0,s}=0\) with zero lift.
For completeness the derivative of the difference in (8) with
respect to \(u\), after this cancellation, is
\[
 g'(u+t)-g'(s-u)-g'(u)+i\pi+2\pi i(u-s).
 \tag{13}
\]
It exponentiates to one using (7). In (9),
\(\arg(1-e^{-2\pi i(u+t)})\in(-\pi/2,\pi/2)\),
\(\arg(1-e^{-2\pi i(s-u)})\in(0,\pi)\), and
\(\arg(1-e^{-2\pi iu})\in(0,\pi/2)\).
For the last assertion use \(\cos(2\pi\Re u)<1/3\)
and \(e^{2\pi\Im u}<e^{\pi/5}<2\), so its real part
is positive.
Together with (12), these put (13) strictly in the strip
\(-2\pi<\Im(\cdot)<2\pi\), so it is zero.
Thus the difference is independent of \(u\).

For every real \(t\in(.278,.391)\), its constant is zero
by the calibrated physical-cap identity at the original critical
\(u_*(t)\), which belongs to the \(u\)-rectangle in (9).
Holomorphy in \(t\) on the connected product proves (8)
throughout (9). The actual prepared root is in this product by
the inherited endpoint images. Chain differentiation of (8),
using \(F_{0,s}=0\), identifies its remaining original equations
and the absolute critical value. \(\square\)

## 3. A regular, strictly accretive four-variable box

Consider the closed box
\[
 \begin{split}
 \widetilde{\mathscr R}={}&
 ([.1,.4]+i[-.12,.12])\times
 ([.22,.5]+i[-.072,.021])\\
 &\hspace{16mm}\times([.2,.42]+i[-.102,.015])^2.
 \end{split}
 \tag{14}
\]
It contains the actual critical point strictly. Its first interval
is the old reduced Newton contour, not the discarded \(s\)-interval.

**Proposition 3.** There is \(\widetilde\mu>0\) such that
\[
             -\Re\widetilde F''\succeq\widetilde\mu I_4
                      \quad\hbox{on }\widetilde{\mathscr R}.
 \tag{15}
\]
This persists on a fixed neighborhood of the box and of the original
output and ordinary-color parameters.

*Proof.* It suffices to check the \((u,t)\) block \(T\);
the remaining terms have exactly the positive allocations in
[the typed-height rectangle theorem](research_mixed_prepared_cap_typed_height_rectangle.md),
Section 2. Write
\[
 a=\Re\cot\pi u,\quad b=\Re\cot\pi t,\quad
 d=\Re\tan\pi u,\quad c=\Re\cot\pi(u+t).
 \tag{16}
\]
Then \(a,d>0\), \(b\ge0\), and
\[
 -\pi^{-1}\Re T''=
       \operatorname{diag}(2d+4a,2b)-c{\bf1}{\bf1}^T.
 \tag{17}
\]
If \(c\le0\), this is positive definite unless \(b=0\)
and \(c=0\). That joint degeneracy is impossible: \(b=0\)
requires \(\Re t=.5\), whereas then
\(.6\le\Re(u+t)\le.9\), so \(c<0\).

If \(c>0\), put \(p_0=\cot(\pi\Re u)\),
\(q_0=\cot(\pi\Re t)\). Then \(p_0,q_0>0\),
\(p_0q_0>1\), and
\[
 c\le\frac{p_0q_0-1}{p_0+q_0},\qquad
 a>\frac38p_0,\qquad b>\frac34q_0.
 \tag{18}
\]
For the first individual bound use
\(\cos(2\pi\Re u)\le\cos(\pi/5)<13/16\) and the
already proved \(\cosh(.24\pi)<13/10\) from
[the symmetric pair-cost proof](research_mixed_terminal_symmetric_pair_costs.md).
The cotangent ratio is then greater than \(5/13>3/8\).
For the second use
\(\cos(2\pi\Re t)<1/5\) and
\(\cosh(2\pi|\Im t|)<\cosh(\pi/5)<5/4\),
the elementary bound used in the
[original cap curvature proof](research_mixed_first_cap_plateau_phase.md).
Its ratio is greater than \(16/21>3/4\).
The rank-one test now gives
\[
 c\left(\frac1{2d+4a}+\frac1{2b}\right)
 <\frac23\,c\left(\frac1{p_0}+\frac1{q_0}\right)
 \le\frac23\left(1-\frac1{p_0q_0}\right)<1.
 \tag{19}
\]
This proves positivity of (17). Compactness gives a uniform
strict floor for \(T\). The old \(V(t,p)\) form is
positive semidefinite, \(V(p,q)\) is positive definite,
\(-g(p)\) and the external incidence add nonnegative forms,
and the chirp has zero real Hessian. This proves (15).
Holomorphy and compactness give the stated persistence. \(\square\)

## 4. Original row symbol and remaining source comparisons

All factorial arguments in (2) stay in their original regular strips
on (14): \(\Re(u+t)\in[.32,.9]\),
\(\Re(t+p)\in[.42,.92]\), and
\(\Re(p+q)\in[.4,.84]\).
The complete Newton factor has the same four-factorial interpolation
as the physical cap theorem, since \(.1\le\Re u\le.4<.5\).
The old outgoing denominator guard
\(|Y|<1,\ |Ye^{-2\pi iq}|<.7\) is unchanged.
Thus the exact lattice rows of (2), including their outside scalar,
have a uniform holomorphic interpolation on a neighborhood of (14).

Put \(a(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2}\), with the
original sine square roots. At complete ordinary color its leading
symbol is \(\kappa^3N^{-3}\widetilde b\,e^{N\widetilde F}\), where
\[
 \widetilde b=
 \frac{e^{\pi iy-\pi iu}\,
       a(u+t)a(t+p)a(p+q)}
 {(2\sin\pi u)\,a(u)^2a(t)^3a(p)^3a(q)
       \sqrt{(1-Y)(1-Ye^{-2\pi iq})}} .
 \tag{20}
\]
Every factor is nonzero. The Newton coefficient contributes
\(N^{-1}e^{NV_0(u)}/(2\sin\pi u)\);
\((-\zeta)^{-a}\) contributes the chosen exponential
\(e^{i\pi Nu}\) and \(e^{-i\pi u}\).
The factorial quotient contributes \(N^{-3}\), whereas
the outside factor \(N^2c_y\) contributes \(N\).
These give the power \(N^{-3}\) in (20).
Four residue constants and the four-dimensional Gaussian give
the unchanged local power \(\kappa^3N^{-1}\).

The source has the three triangular support walls
\(u+t=1,t+p=1,p+q=1\); exact equality rows remain zero.
Its four coordinate-zero faces are also retained.
Its physical entropy and its private cuts/aliases are those of
this new chart. The old failed \(s=.49\) comparison is not one
of them. Conversely, old passed contour comparisons are not
automatically new comparisons for (2).
The complete real-index \(U_0\) packet and its
[right extension](research_mixed_physical_three_cap_right_extension.md)
may be used on physical \(t\)-slices before modulus. Off-grid
deformations instead use the literal rows in (2) and their
interpolation just established.

This theorem supplies exact regrouping, original action calibration,
and global regularity and curvature on (14). It asserts no sign for
the new physical complement, zero-mode joins or horizontal/vertical
aliases, no identity of independently chosen local Gaussian cycles,
and no full-period propagation or whole mixed-word conclusion.
