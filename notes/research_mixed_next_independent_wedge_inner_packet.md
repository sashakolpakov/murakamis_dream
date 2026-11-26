# An independent wedge and an open neighborhood for the inner packet

Private finite-source extension, 9 November 2026. The completed
right-current proof depends on independent angle and depth bounds,
not on the outer selected critical equation. It therefore proves
the inner packet on a two-dimensional wedge. An independently
proved full-disk bridge at zero then gives a genuine open
neighborhood of the entire selected curve, with holomorphic
normalized errors and fixed derivative bounds.

No mathematical numerical evaluation, saved-value arithmetic,
or frozen-source edit is used. This is an inner-source theorem;
it does not estimate the remaining outer observation.

## 1. Independent domain and statement

Put
\[
 \mathcal W=\{\beta-iK:
     0\le\beta\le8/7,\quad0\le K\le2/5,\quad K\le\beta/2\}.
\tag{1}
\]
Use the original cubic continuation on
\(\mathcal U_+=\{0\le\Re u\le\pi/2,\ -1/2\le\Im u\le0\}\).
It supplies \(t_*(u)=a_*(u)-iH_*(u)\), the calibrated
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,
 \qquad S(u)=\Phi(t_*(u),u),\quad s(u)=\Re S(u).
\tag{2}
\]
The functions \(t_*,S\) are holomorphic on a neighborhood
of \(\mathcal U_+\).

Keep exactly \(Q_N^{\rm sh}\), \(Q_N^{\rm full}\),
\(C_{N,3}\), and \(\mathcal A\) from
[the selected-curve assembly](research_mixed_next_selected_curve_inner_packet.md)
and [the outgoing-tail restoration](research_mixed_next_outgoing_tail_trace_restoration.md).
Thus the first edge and full inner trace are unchanged.
The superscript \({\rm sh}\) shortens only the second
edge to \(U=\lfloor N/2\rfloor-1\).

**Theorem.** Uniformly on the entire closed wedge \(\mathcal W\),
at both parities,
\[
 Q_N^\star(u)=
 C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                          \{1+O(N^{-1})\},
                 \qquad \star\in\{{\rm sh},{\rm full}\}.
\tag{3}
\]
Moreover there is a fixed open set \(\Omega\) containing
\[
             \mathcal C=\{u_\delta:0\le\delta\le1/2\}
\]
on which both sources have the same packet with
holomorphic normalized \(O(N^{-1})\) remainder. On a
fixed smaller open neighborhood of \(\mathcal C\), every
fixed complex derivative of either normalized remainder
is also \(O(N^{-1})\), uniformly through both parities.

All these sources are nonzero for sufficiently large
\(N\) on a common smaller neighborhood. No value of
its radius is claimed or evaluated.

## 2. All original parameter guards on the wedge

The inequalities needed in the right-current proof can be
verified for every independent \(u\) in (1).
For \(\beta>0\), the elementary positive and alternating
series give
\[
 \sinh K\le\frac{24}{23}K
       \le\frac{12}{23}\beta
       <\frac{19}{27}\beta\le\sin\beta .
\tag{4}
\]
Here \(K\le2/5<1/2\), \(\beta\le8/7<4/3\), and
\(12/23<19/27\). Consequently
\[
 |\cos u|^2=\cos^2\beta+\sinh^2K<1,\qquad
 \Re\cos u>7/30,\qquad \Im\cos u\ge0.
\tag{5}
\]
At \(\beta=0\), (1) forces \(K=0\), and the weak modulus
bound remains valid. In particular the original guards
\[
 B=\cos^2(u/2),\quad
 \Re B>37/60,\quad |B|^2\le\Re B,\quad
 |1-B|<9/20,\quad \Im B\ge0
\tag{6}
\]
hold on all of \(\mathcal W\).

The stronger actual first-height bound also holds independently:
\[
                         2/3<H_*(u)<1.
\tag{7}
\]
Indeed the original cubic root \(v=2\cos(t_*/2)=x+ib\)
has \(x>3/2\), \(1/3<b<2/3\), and
\[
 (3b-2)x^2-b^3+2b^2-3b+2=2\Im\cos(u/2)\ge0.
\tag{8}
\]
For fixed \(x\) its left side increases in \(b\), and at
\(b=1/2\) is \(-x^2/2+7/8<-1/4\). Thus \(b>1/2\).
The same original argument as in the selected cut-guard
proof, using
\(b<\sqrt2\sinh(H_*/2)\),
\(\sqrt2<10/7\), and \(\sinh(1/3)<18/53\), proves
\(H_*>2/3\). The upper bound and \(0<a_*<\pi/2\)
are the original cubic theorem on \(\mathcal U_+\).

The real-then-vertical integration in
[the action-floor proof, Section 2](research_mixed_next_selected_action_floor_and_endpoint_payment.md)
uses only
\(\beta\le8/7\), \(K\le2/5\), and the whole cubic guards
\[
 \Re c>3/4,\quad1/6<\Im c<1/3,\quad
 |c|^2<127/144,\qquad c=\cos(t_*(u)/2).
\]
It never uses the outer critical equation defining \(u_\delta\).
Its strict rational inequalities therefore give on (1)
\[
                       s(u)>\frac{2651}{1600}>\frac{331}{200}.
\tag{9}
\]
Allowing equality in the two upper bounds in (1) does not
remove the strict reserve: the cosine, logarithm, tangent,
and \(\pi\) comparisons in that proof remain strict.
Likewise its endpoint-sector proof applies whenever
\(\pi/2\le a\le2\pi/3\), \(2/3\le H\le1\):
\[
 \Re\psi(a-iH,0)+\frac{H+K}{2}
                      +\frac{3aH}{2\pi}-H<\frac{33}{20}.
\tag{10}
\]

## 3. The boundary case \(K=0,\ \beta>0\)

This case must be checked explicitly when extending the
finite upper-envelope proofs. Their selected-curve version
has \(K=0\) only at \(u=0\).

If \(K>0\), all their original bottom and side arguments
apply directly by (5)--(7). If \(K=0,\beta>0\), the outgoing
upper zero cut lies on the real bottom and starts at
\[
                          x_\beta=\frac12-\frac{\beta}{2\pi}.
\tag{11}
\]
For \(0<x<x_\beta\), the outgoing derivative
\[
 e^{b_y(x,\beta)}
            =\frac{\cos(2\pi x)+\cos\beta}{1-\cos(2\pi x)}
\]
is positive real with its original zero argument. The incoming
leg has its original argument in \((0,\pi)\), because its
angle is between \(\pi/2\) and \(a_0<\pi\) and its depth
is positive. Hence the full upper envelope has strictly
negative inward normal derivative on this part of the bottom.

For \(x\ge x_\beta\), do not assert that same normal sign.
Instead the original outgoing-cut estimate applies at
\(\cosh K=1\), including its starting zero:
\[
 \left|\frac{(\cos2\pi y+\cos t)(\cos2\pi y+\cos u)}
                 {(1-\cos2\pi y)^2}\right|
                   \le\frac{13\sqrt{79}}{150}<1 .
\tag{12}
\]
Its proof requires only \(\beta<\pi/2\),
\(\cosh K\le8/7\), and \(|\cos t|<8/5\),
which hold on all the three source families used below.
Thus the bottom envelope decreases strictly horizontally
on this cut. At its starting zero the same one-sided
decrease follows from the original zero-safe logarithm.
There is no bottom local minimum anywhere.

All side formulas remain unchanged. The right-side minimum
is at \(\min(H,K)/(2\pi)=0\); above zero, the outgoing
leg contributes derivative \(\pi\), while the incoming
uncrossed leg contributes more than \(-\pi\).
Thus the full right side increases strictly. The left
side increases as before. Every strict side sublevel
is connected or empty. This verifies the only new
boundary configuration; it makes no change to a logarithmic
lift or to a finite endpoint group.

## 4. Uniform finite source and four-piece path on the wedge

Here are the three second-edge source families:
\[
\begin{array}{ll}
\text{high horizontal:}&
 \pi/2\le a\le2\pi/3,\quad 2/3\le H\le1,\\
\text{vertical:}&
 a=2\pi/3,\quad1/10\le H\le1,\\
\text{low horizontal:}&
 2\pi/3\le a\le a_0,\quad H=1/10.
\end{array}
\tag{13}
\]
The proofs in the corresponding
[high envelope](research_mixed_next_selected_right_edge_upper_envelope.md),
[vertical envelope](research_mixed_next_selected_right_edge_vertical_upper_envelope.md),
and [initial low-horizontal theorem](research_mixed_next_selected_initial_low_horizontal.md)
extend to all \(u\in\mathcal W\) as follows.

Their cut-force inequalities use (5), the displayed first
angle/depth ranges, and \(\cosh K<8/7\). Their \(A,B,D,W\)
guards use (6). The original principal wire saddle and
zero logarithmic charge start from the already proved
mixed/positive edge at \(a=\pi/2,H=H_*(u)\), which is
available for every \(u\in\mathcal U_+\).
Continue first in \(H\), then in \(a\), exactly as in
the respective source proofs. The strict cut-force
guards and nonzero Hessian prevent a charge change.
The saddle value remains the same calibrated \(\psi(t,u)\).

The upper envelope remains continuous and subharmonic,
with the original positive jumps and zero starting-point
flux. Section 3 supplies the bottom condition when the
outgoing cut reaches the real line. The side traces and
uniform large-height growth have the same signs and
constants. The component/Jordan argument therefore
constructs the same upper paths at rate
\(\max\{\Re\psi(t,u),(H+K)/2\}\), up to a fixed tolerance.
The parameter families are compact. Finite path covers,
rather than a globally continuous path choice, give
uniform lengths, heights, and tolerances.

The literal reciprocal-factorial interpolation is unchanged.
Its shifted real arguments retain a fixed margin inside
\((-1,1)\); its zero-safe physical endpoint bounds include
all rows \(0\le j\le U\). The two complete aliases, midpoint
caps, exact residue factors \(N\), and both oriented
unweighted endpoint connectors are those displayed in
the source proofs. Their bounds use only the same
angle/depth ranges and (5)--(6), including the deeper
height-two reserve on the last two families.
Thus the complete second-edge estimate
\[
 |K_N^<(t,u)|\le C_\tau
 \exp N\{\max(\Re\psi(t,u),(H+K)/2)+\tau\}
\tag{14}
\]
holds uniformly on all three families (13), for every
\(u\in\mathcal W\). No source group is omitted at \(K=0\).

The rate comparisons likewise require no outer stationarity.
On the high horizontal, (7),(9),(10) and the original
inner concavity apply. Its compact gap uses
\[
 d_{\mathcal W}=\pi/2-\max_{\mathcal W}a_*(u)>0 .
\]
The low geometric endpoint proof in
[vertical payment, Section 2](research_mixed_next_selected_inner_vertical_payment.md)
uses only \(\beta\le8/7\), \(K\le2/5\), \(K\le\beta/2\)
and the original closed primitive. The strict estimates
still give \(\Re\Phi(2\pi/3-i/10,u)<8/5\).
The same height convexity and endpoint-sector monotonicity
pay the vertical. The return derivatives pay the initial
low horizontal. Finally the
[far-horizontal proof](research_mixed_next_selected_low_far_horizontal.md)
uses only \(K\le2/5\) and the real complete-period slit
bound, and retains rate less than \(329/200\);
the strict first-action reserve is unchanged at \(K=2/5\).

Consequently the exact four-piece contour identity in
[the curve assembly, (12)--(17)](research_mixed_next_selected_curve_inner_packet.md)
now proves a uniform positive gap for its full remaining
current on \(\mathcal W\).
The earlier single-current representation was already
uniform on \(\mathcal U_+\), which contains \(\mathcal W\).
Its complete partial Gaussian, first-edge trace tail,
negative currents, physical normals and endpoint verticals
therefore need no extension. Applying the same relative-error
division proves (3) for \(Q_N^{\rm sh}\) on the whole wedge.

For the full source, the independent finite difference theorem
gives on this wedge
\[
 |Q_N^{\rm full}(u)-Q_N^{\rm sh}(u)|
       \le C N^A e^{47N/30}.
\tag{15}
\]
Equations (9),(15) leave a gap greater than \(53/600\)
before polynomial absorption. Adding this difference
therefore proves (3) for \(Q_N^{\rm full}\), with exactly
the same action and amplitude.

## 5. Genuine open-neighborhood packet

Let
\[
 \mathcal W^\circ=
 \{0<\beta<8/7,\quad0<K<2/5,\quad K<\beta/2\}.
\tag{16}
\]
This is an open subset of the complex \(u\)-plane.
The original local edge packets at \(t_*(u)\), the nonzero
inner Hessian, and their calibrated roots make
\(\mathcal A\) holomorphic and nonzero on a neighborhood
of \(\mathcal U_+\). More precisely,
[the complete edge-neighborhood theorem, Section 7](research_mixed_next_shortened_edge_upper_continuation.md)
gives the holomorphic nonzero second-edge amplitude on
a fixed independent neighborhood of the whole cubic graph.
The original complete first-edge packet gives the same
property for the first factor. The coefficient in
[the partial horizontal packet](research_mixed_next_inner_three_partial_horizontal_packet.md)
is their product with the original nonzero inner Gaussian
factor. This proves the stated property of \(\mathcal A\);
it does not differentiate a chosen family of contours.
On \(\mathcal W^\circ\),
the normalized functions
\[
 \mathcal E_N^\star(u)=
 \frac{Q_N^\star(u)}
      {C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}}-1
\tag{17}
\]
are therefore holomorphic. The uniform wedge proof gives
\(|\mathcal E_N^\star|\le C/N\) there, not merely on a
one-dimensional set.

At zero, Section 5 of
[the outgoing-tail restoration](research_mixed_next_outgoing_tail_trace_restoration.md)
proves a full-disk packet for both sources on some
fixed \(|u|<\rho\). Its action and amplitude agree with
the original ones in (17) on the overlap, by their
source normalization and the identity theorem.
Shrink \(\rho>0\) if necessary so all these normalizations
remain holomorphic and nonzero.

Thus
\[
                   \Omega=\mathcal W^\circ\cup\{|u|<\rho\}
\tag{18}
\]
is an open set on which both normalized errors in (17)
are holomorphic and uniformly \(O(N^{-1})\).
Every selected \(u_\delta\) with \(\delta>0\) lies
strictly inside \(\mathcal W\), by the adopted strict
angle and depth guards. The zero-charge point belongs
to the disk. Hence the entire compact curve
\(\mathcal C\) lies in \(\Omega\).

Choose \(r>0\) so that the closed \(2r\)-neighborhood
of \(\mathcal C\) is contained in \(\Omega\).
Such a fixed \(r\) exists by compactness. For points
in the \(r\)-neighborhood, the Cauchy circle of radius
\(r\) remains in \(\Omega\). Thus for every fixed
integer \(j\ge0\),
\[
       |\partial_u^j\mathcal E_N^\star(u)|
                         \le \frac{j!\,C}{r^jN}.
\tag{19}
\]
This proves the open-neighborhood and normalized derivative
assertions, and uniform nonvanishing for sufficiently large
\(N\). The set (18) is not claimed to contain a full horizontal
outer contour, either sign of every complex angle, or any
larger prescribed rectangle.

This extension uses a two-dimensional finite-source estimate
and a separately proved full-disk bridge. It does not infer
an analytic packet from physical samples, from curve values,
or from formal critical-point continuation.

## Frozen source bindings

- Original selected-curve packet and exact contour assembly:
  e3bc75e93e1c1834faa920ff2f4ef0711c8f6cc7906b6c0c5b59bbadc86f57b7.
- Outgoing-tail finite difference and local disk bridge:
  8b30fb2a8258d49fd8c162d5822c4652129ffc5a39ee77019e1b00aa2db7596e.
- Original whole cubic and calibrated action:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Original one-current source:
  2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421.
- Original independent second-edge neighborhood and amplitude:
  b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542.
- Original partial Gaussian and its coefficient:
  03482ac7f06246db3c162965360e8f3ff596b1339b1b07522cc4947f149aa8ad.
- Selected angle-depth correlation:
  49d0d81bb39dcdb8946893c8bc0b712e00b2eaad15b3f5476b62736fce1df1f4.
- Selected upper depth:
  f3b0b8f8e14adb8beff461e53ec20cdcb7afb4dc07bda3e1247116b55e13c017.
- Actual cut guards:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Action floor and high-horizontal payment:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Complete high envelope:
  c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699.
- Complete vertical envelope:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.
- Complete vertical payment:
  5813ddfa3f16e81c7907bbf8e11f6be0d07d30e0e71a74f5845d889aa1a4ac85.
- Complete initial low horizontal:
  2f0287cf9655c04d2b9ca0a1545707619b57f23e899c3b76430c73b143929141.
- Complete low far horizontal:
  1cb4d220d4fbf5fddeaf9ecb24b572908a4485e907ac4634ea2623acee0b34bd.

