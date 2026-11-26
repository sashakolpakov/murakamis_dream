# Closing phases and the limits of the charged variational bound

Private written deduction, 14 November 2026. Only written identities
are used. No numerical calculation, test, or frozen-file change is
part of this argument.

The phase-sensitive charged upper bound retains substantial
cancellation inside proper-length blocks. It does not retain all
closing or clock cancellation. This can be seen in the exact Markov
operation, which is a scalar operator before any exterior is attached.
The calculation below identifies the missing information and the
corresponding stationary equations. It is not a counterexample to a
volume conjecture or to a bound restricted to a separately specified
reduced hyperbolic presentation.

## 1. Full-length closing blocks are invisible to the limiting arc loss

Use the functions from
[the charged block theorem](research_charged_block_holonomy_rate_loss.md):
\[
 I_{\lambda,\rho}(\theta)=\frac1{2\pi}
 \int_{-\pi\lambda}^{\pi\lambda}
                   \log|1+\rho e^{i(\theta+s)}|\,ds.
\]
For every \(\rho>0\),
\[
 I_{1,\rho}(\theta)=\log\max(1,\rho),\qquad
 I_{0,\rho}(\theta)=0.                                    \tag{1}
\]
The first identity follows by integrating the logarithmic series
for \(\rho<1\), applying inversion for \(\rho>1\), and taking
the integrable limit at one. In particular both endpoint lengths
have zero angular loss at every phase.

Call a block proper when \(0<\lambda_e<1\). If the graph of
proper blocks is a forest, vertex phases can align every proper
block simultaneously: choose a phase at one vertex in each tree
and propagate along its edges. All other arc terms are independent
of phase by (1). Therefore
\[
 \max_{\vartheta}\sum_e
 I_{\lambda_e,r_v/r_u}(\omega_e+\vartheta_v-\vartheta_u)
                  =\sum_e I_{\lambda_e,r_v/r_u}(0)          \tag{2}
\]
at every radius. More generally the same statement holds if the
proper-block connection is flat. A cycle using a full-length
closing block can have nontrivial holonomy without changing (2).

This is a structural limitation of the limiting functional, not
an omitted term in its proof. Every finite closing block and its
pivot are still present in the exact source. Its length is
\(N-1\), whose normalized limit is one. That limit can lose an
exact root zero of a Fourier coefficient while correctly retaining
the logarithmic upper bound on the polynomial's modulus.

## 2. The Markov crossing is scalar before exterior contraction

Put \(d=N-1\), \(q=e^{\pi i/N}\), and
\(A_N=q^{-1/2}\), with the specified exponential square root.
In the external basis let
\(K_{\rm ext}e_i=q^{2i-d}e_i\). The original crossings satisfy
\[
 \begin{split}
 \operatorname{Tr}_2[(I\otimes K_{\rm ext})R_{{\rm ext},+}]
                       &=q^{-d-d^2/2}I,\\
 \operatorname{Tr}_2[(I\otimes K_{\rm ext})R_{{\rm ext},-}]
                       &=q^{d+d^2/2}I.                     \tag{3}
 \end{split}
\]

Here is a finite operator proof, with the boundary indices retained.
The [regular crossing adapter](research_rivin_jones_local_crossing_adapter.md)
identifies the external crossings with the physical braided
intertwiners of opposite sign and transports \(K_{\rm ext}\)
to the physical \(K\). The partial-trace computation in
[the prescribed-cut theorem](research_rivin_jones_prescribed_cut_and_hermite_recovery.md),
Section 2, proves directly that the \(K\)-weighted partial trace
of such an intertwiner commutes with \(E,F,K\). Its proof uses
the displayed coproducts and cyclicity only in the traced factor.
The physical \(K\) has distinct eigenvalues and the adjacent
lowering arrows are nonzero. Hence this partial trace is scalar.

The scalar can be evaluated in a single boundary coordinate. The
external positive crossing sends
\((i,j)\) to \((j+t,i-t)\). When the retained input is \(i=0\),
the trace forces \(t=j=0\). The crossing entry is
\(A_N^{d^2}\), and the pivot is \(q^{-d}\), giving the first
line of (3). The negative crossing sends \((i,j)\) to
\((j-t,i+t)\). At retained input \(i=d\), the trace forces
\(j=d,t=0\). Its crossing entry is \(A_N^{-d^2}\), and its
pivot is \(q^d\), giving the second line.

Consequently an arbitrary exterior operator acting on the retained
heads can be left in place: tracing the added head replaces its Markov
crossing by the corresponding scalar in (3). No assumption that
the exterior is scalar, or that its marked row may be averaged,
is needed for this local replacement. In the original physical
convention \(g=K/s\), \(x=q^d=-q^{-1}\), \(s=x^N\), and
\(\kappa=q^{d^2/2}\), a positive physical crossing has scalar
\(\kappa x/s\). Its prescribed framing cancels this unit factor.

## 3. Exact clock cancellation in the closed Markov operation

The same operation can be inspected in the original charged
representation, without changing its clocks. Consider the positive
physical Markov crossing with its original two closing adapters.
Write \(X\) for its over-input, \(Z\) for its over-output,
and \(Y\) for its under-input. The under-output is
\(xQ^{-h}Y\), where \(Q=q^2\), \(0\le h\le d\).
The two crossing blocks have lengths \(d-h,h\); their directed
anchor pairs are \(X\to Y\) and \(Y\to Z\). The two closures
are \(Y\to X\) and \(Z\to Y\), each of length \(d\).

The exact gains, obtained from equations (7),(17),(18) of
[the charged source](actual_global_charged_bridge_flow.md), are
\[
 w_0=q^{d-h},\qquad w_1=q^{h-d},\qquad
 w_A=q^{2h-d},\qquad w_B=q^{-2}.                           \tag{4}
\]
The last gain is the actual pivot. Let \(a,b\) be the head
charges of the two crossing blocks. Conservation forces the
closing head charges to be \(h+a,b\), respectively. All
\(0\le a\le d-h\) and \(0\le b\le h\) are admissible.
Closing block coefficients have magnitude one. Apart from the
specified unit factors independent of \(a,b\), the entire
fixed-clock coefficient is therefore
\[
 w_A^h B_{d-h,N}(w_0w_A)B_{h,N}(w_1w_B)
       =w_A^h B_{d-h,N}(q^h)B_{h,N}(-q^{h-1}).              \tag{5}
\]
This is a sum over the complete source support, not a selected
subset. The finite product formula gives
\[
 \begin{split}
 B_{h,N}(-q^{h-1})&=\prod_{r=0}^{h-1}(1-Q^r),\\
 B_{d-h,N}(q^h)&=\prod_{r=h+1}^{d}(1-Q^r).
 \end{split}                                                \tag{6}
\]
Thus every \(h\ge1\) coefficient vanishes exactly. At \(h=0\)
the second product in (6) is \((Q;Q)_d=N\), and the first is
one. Restoring \(\chi_N/N\) and the original unit factors gives
the scalar \(\chi_N\kappa x/s\), in agreement with (3).
All levels and both parities are included. The cancellation occurs
already inside a fixed nonzero clock sector; it need not wait for
the final sum over clocks.

Nevertheless the limiting upper functional in
[the angle-optimization theorem](research_charged_source_angle_optimization.md)
has strictly positive value for this same presentation. Write
\(t=h/N\) in the limit and
\[
 b_\lambda(y)=I_{\lambda,e^y}(0).
\]
The proper blocks form a path, so (2) applies. Set the \(X\)
radius to one, the \(Y\) radius to \(e^u\), and the \(Z\)
radius to \(e^{u+v}\). Direct substitution in that theorem's
functional gives
\[
 \mathcal A_t(u,v)=
 t u+b_{1-t}(u)+\max(0,-u)
                    +b_t(v)+\max(0,-v).                   \tag{7}
\]
The two radius minima are at zero. First take \(0<t<1\).
Equation (16) of that theorem shows that \(b_\lambda'\) lies in
\([0,\lambda]\), with \(b_\lambda'(0)=\lambda/2\), for
\(0<\lambda<1\). Each term in (7) is convex;
its one-sided derivatives at zero enclose zero. Hence
\[
 \inf_{u,v}\mathcal A_t(u,v)
   =b_t(0)+b_{1-t}(0)
   =-2J(t/2)-2J((1-t)/2).                                 \tag{8}
\]
The endpoint lengths follow directly from (1), or by continuity.
The derivative of the last expression is
\(\log\cot(\pi t/2)\), so its maximum is at \(t=1/2\).
If \(v_8\) denotes the regular ideal octahedron volume, then
\[
              \sup_{0\le t\le1}\inf_{u,v}\mathcal A_t(u,v)
                    =-4J(1/4)=\frac{v_8}{2\pi}>0.          \tag{9}
\]
The trivial one-head presentation has upper rate zero. Thus the
variational functional is not Markov invariant, even though its
finite source is. No positive loss from the full-length closing
phases survives in (7). Equation (9) does not prove that an arbitrary
attached hyperbolic exterior suffers this same additive excess;
its coupled optimization would require a separate argument.

## 4. The missing half of the joint stationary equations

The same loss can be located before any topological interpretation.
On a regular complex block chart let \(z\) denote logarithmic
anchor coordinates, so \(z_a=\log r_a+i\vartheta_a\), and let
\(H(\lambda,z)\) be the holomorphic leading action of the anchor integrand, including
the real clock-factor contribution \(-\sum_eJ(\lambda_e)\)
and the original coefficient loads. The extracted clock and block
phases contribute another term \(i\phi(\lambda)\). Both are
fixed by the original source; \(\phi\) is not adjustable.

Where the anchor phase maximum and radius minimum are smooth and
interior, their first-order equations are
\[
 \operatorname{Re}\partial_z H=0,\qquad
 \operatorname{Im}\partial_z H=0.                           \tag{10}
\]
The second equation follows by differentiating in the anchor
arguments, since \(\partial_\vartheta\operatorname{Re}H
=-\operatorname{Im}\partial_zH\). Thus the anchor optimization
retains complex anchor stationarity. At an interior smooth maximum
over lengths, envelope differentiation in an allowed real length
direction \(v\) gives only
\[
                    \operatorname{Re}\,d_\lambda H[v]=0.
                                                               \tag{11}
\]
The full original clock saddle additionally requires, with its
actual lattice character retained,
\[
 \operatorname{Im}\,d_\lambda H[v]+d\phi[v]
                \quad\text{to equal the corresponding Fourier
                lattice character}.                        \tag{12}
\]
In primitive integer clock coordinates that character is an
integer multiple of \(2\pi\). In dependent length coordinates
one must use the induced lattice, rather than assigning unrelated
integers to all block lengths.

The variational upper bound is unchanged if the extracted unit
clock factors are changed, while (12) changes. This statement
describes exactly which factors its proof takes in absolute value;
it does not propose changing the invariant. The original feedback
equations (15)--(16) in
[the clock-feedback normal form](actual_clock_feedback_normal_form.md)
retain these terms. A geometric identification based only on
(10)--(11) would omit source equations. The Markov calculation
also shows that even the anchor coefficient can have exact root
cancellation not measured by a limiting maximum-modulus bound.

The constructive conclusion is that exact local contractions such
as (3) and (6) should be performed before this optimization when
available. A genuinely joint geometric contour must retain (12),
all closing factors, and their original relative cycle. The current
upper bound remains valid and useful, but its value cannot be
declared a topological volume merely from its concave angle dual.

## Direct source versions

| Source | SHA-256 |
| --- | --- |
| actual_global_charged_bridge_flow.md | b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c |
| research_rivin_jones_prescribed_cut_and_hermite_recovery.md | 1b0e105ffb67b2b8552f5fddc5f0a3ac009e9795b33e27599ac4726ebd74079e |
| research_rivin_jones_local_crossing_adapter.md | c4a9a92ec22f31a035036642e0621ef9abe569646b2488dbac2d2add786500f0 |
| research_charged_source_angle_optimization.md | 45b21fabb9cb65512bc3e576eb3d659b6fe14c3dcd90b4164bfdb12b8cedea64 |
| research_charged_block_holonomy_rate_loss.md | dfd2cae48cd534a12602670145ee09c3c959cf663e304e62896d4b47e1184b6e |
| actual_clock_feedback_normal_form.md | f58a4dfd06615ecace95959e58474837f7eb50ef7f01a3c00d517d3938cb06bf |
