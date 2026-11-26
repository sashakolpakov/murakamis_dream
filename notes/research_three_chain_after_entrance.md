# Volume growth for chains of three-crossing blocks

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

For every fixed length \(m\ge10\), the original finite word
\(v(-2)^TA_N^m v(-2)\) has a nonzero leading asymptotic and its
exponential growth is the volume of \(M_m\), the original marked
positive partial filling with both outside ends complete. The ordinary
complete boundary color is \(-2\) at each end. The theorem retains
every fixed ordinary derivative at these colors and both level
parities. It is a theorem about this scalar source; identifying a knot
invariant requires the separate original marked closure and component
conditions. The construction below does not supply lengths three
through nine. The separate
[larger closing theorem](research_three_larger_source_closure.md)
now extends the original-source conclusion to every fixed \(m\ge6\);
the proof below records the small-class route and its length count.

## 1. The proved source induction and the entrance source

Use
\[
 A_N=JM^3,\qquad
 \widetilde A_N=A_N-E_{\lfloor N/40\rfloor},\qquad
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 k_0=\frac{4\pi}{21}(2\sqrt3-3i),
 \quad R=\frac1{200}.
 \tag{1}
\]
Put
\[
 \rho=\frac{5-\sqrt{21}}2,
 \qquad Z=\frac{(21/20)\rho}{1-(3/10)\rho},
 \quad A_0=\frac{29}{20},\qquad
 d_r(t)=\min\{\operatorname{dist}(t,\mathbb Z),r\}.
 \tag{2}
\]
All phases below are the actual continued phases, including their
original additive constants.

**Proved input (broader actual-source induction).** Suppose an actual
finite half-band source has a nonzero holomorphic packet on a
neighborhood of the following internal Fourier domain, at its fixed
complete ordinary outside colors:
\[
 x_h+\bigl(\{|z|\le R\}\cup[-.009,.009]\bigr),
 \qquad S'(x_h+z)/k_0=-\sqrt{21}z+h(z),
 \quad |h(0)|\le H\le.0057,\quad |h'|\le.18,
 \tag{3}
\]
and its full real period satisfies
\[
 |F_N(x_h+t)|\le CN^b
 e^{N[\Re S(x_h)+|k_0|H d_{.03}(t)-A_0d_{.03}(t)^2]}.
 \tag{4}
\]
Assume also the corresponding packets and the same exponential
envelope, with order-dependent polynomial factors, for every fixed
ordinary outside-color derivative evaluated at those complete colors.
No uniform global envelope on an outside-color neighborhood is assumed.
Then the exact attachment
\[
 F_{N,+}(y)=N\int_{x_h-1/2}^{x_h+1/2}
                 F_N(x)h(x)^T\widetilde A_Nh(y)\,dx
 \tag{5}
\]
again has (3)--(4), with the actual critical phase, nonzero
amplitude, the same power of \(N\), and certified gradient bound
\(H_+=ZH\). Each attachment multiplies the original unit carrier
by \(\kappa\). The assertion includes both level parities and
preserves these fixed ordinary derivatives at completeness. The packet
remains uniform and holomorphic in the internal Fourier variable.
In particular it bounds every complementary part of the full period;
a local phase transform is insufficient.

This is Theorem 1 and the fixed-jet conclusion of Corollary 2 in the
[full larger-source propagation theorem](research_three_larger_source_propagation.md).
Its proof retains the entire original period, establishes the nonzero
coefficient, and resets the global envelope after every attachment.
The [larger analytic class](research_three_larger_phase_class.md)
supplies its critical branch and derivative estimates.

The initial source required by (3)--(4) is already supplied by
the [real extension of the first additional attachment](research_three_first_entrance_real_extension.md):
\[
 F_N^{[3]}(y,w)=v(w)^TA_N^3h(y),\qquad H_0=.0057,
 \tag{6}
\]
with power \(N^{-1}\) and original carrier
\(C_{N,3}\kappa^2\). Here
\[
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)},\qquad
 \kappa=e^{\pi i(N-1)^2/(2N)}.
 \tag{7}
\]
The ordinary complete color is \(w=-2\); it has not been
replaced by a homogeneous Fourier endpoint. Its full-period envelope
is available at that color and for each fixed ordinary derivative
there. This does not supply a uniform envelope on a fixed complex
outside-color neighborhood.

## 2. Two more attachments enter the proved small class

After two applications of the proved induction, the literal source is
\[
 F_N^{[5]}(y,w)=v(w)^TA_N^3\widetilde A_N^{\,2}h(y).
 \tag{8}
\]
It has a nonzero packet on the union (3), power \(N^{-1}\),
carrier \(C_{N,3}\kappa^4\), derivative defect at most `.18`,
and gradient bound
\[
            H_2=Z^2(.0057)<.000312<\frac1{2500}.
 \tag{9}
\]
Its envelope still uses the larger distance cap `.03`.
For \(H\le1/2500\), the function
\(f_H(v)=|k_0|Hv-A_0v^2\) is strictly decreasing for
\(v\ge.01\), since
\[
                 2A_0(.01)-|k_0|/2500>0.
 \tag{10}
\]
Thus \(f_H(d_{.03}(t))\le f_H(d_{.01}(t))\) on the entire
period. Restricting the packet to the disk, (8) satisfies every
hypothesis of the already proved
[small-source induction](research_three_source_tail_propagation.md).
That theorem may now be applied any further fixed number of times.

The single-step certified bound \(Z(.0057)>1/2500\) does not
establish entry into that small class. Consequently the two steps
in (8) are the preparation count justified by these constants.
This is a threshold for this argument, not a claim that shorter
chains lack a nonzero leading term.

For each fixed integer \(j\ge0\), the resulting left source is
\[
 F_{j,N}(x,w_L)=v(w_L)^TA_N^3
                        \widetilde A_N^{\,2+j}h(x).
 \tag{11}
\]
It has power \(N^{-1}\), carrier
\(C_{N,3}\kappa^{4+j}\), and the small-class envelope and
packet. The same construction applies independently at the right
complete end.

## 3. Exact closure and the length count

The bilinear cardinal identity holds at both parities on every
horizontal period:
\[
                     N\int h(x)h(x)^T\,dx=I.
 \tag{12}
\]
Moreover \(A_N^T=A_N\) and
\(\widetilde A_N^T=\widetilde A_N\). Therefore the exact
closure of (11) with the right source having \(k\ge0\) further
attachments is
\[
 \begin{split}
 \mathcal Q_{j,k,N}(w_L,w_R)
 &=N\int F_{j,N}(x,w_L)F_{k,N}(x,w_R)\,dx\\
 &=v(w_L)^TA_N^3\widetilde A_N^{\,4+j+k}A_N^3v(w_R).
 \end{split}
 \tag{13}
\]
The right word is transposed and reversed before the identical
retained factors are combined. No complex conjugation or positivity
of the open-chain scalar is used.

The total selected-vertex count is
\[
                          m=10+j+k.
 \tag{14}
\]
Thus every integer \(m\ge10\) occurs, for example with
\(j=m-10,k=0\). Both caps are prepared; preparing only one
end would not satisfy the closing theorem.

By the [full small-source closure](research_three_small_source_closure.md),
there are local holomorphic phase and amplitude germs \(\Xi_m,a_m\)
at the two ordinary complete colors, with \(a_m(-2,-2)\ne0\), such
that at \(w_L=w_R=-2\),
\[
 \mathcal Q_{j,k,N}
   =C_{N,3}^{2}\kappa^{m-2}N^{-3/2}
       a_m(w_L,w_R)e^{N\Xi_m(w_L,w_R)}(1+O(N^{-1})).
 \tag{15}
\]
The original \(N\,dx\) in (13), two cap powers \(N^{-1}\),
and one wire Gaussian \(N^{-1/2}\) give \(N^{-3/2}\).
The carrier is the product
\((C_{N,3}\kappa^{4+j})(C_{N,3}\kappa^{4+k})\), exactly as
displayed. It has modulus one and retains both level parities.
All factors of the local amplitude are nonzero; the proved absolute
complementary gap prevents their leading term from being cancelled.
The corresponding differentiated asymptotic holds for every fixed
ordinary derivative at \((w_L,w_R)=(-2,-2)\). To obtain this jet
version of closure, differentiate the exact finite integral first.
Every complementary estimate keeps its strict exponential gap because
the derivative hypotheses change only polynomial factors. On the
central contour, the uniform internal Fourier packets and their
ordinary jets give the differentiated stationary-phase expansion.
This argument does not infer a uniform full-source asymptotic on a
fixed complex neighborhood of the outside colors from pointwise jets.

## 4. Geometric identification, absolute normalization and restoration

Each critical operation in (5) or (13) is stationary elimination
of the original cap-plus-retained phase. Restoring its hidden cap
angle and retained index variables therefore gives a stationary
point of the full unsummed phase \(\mathcal G_m\) in the
[all-length chamber theorem](research_three_chain_geometric_chamber.md).
The two initial prepared caps use their certified cap and index
branches. All additional critical wires stay inside the disk of
radius \(R\), and the retained kernel uses its same original
selected index branch. These are inside the common central wire,
index and cap sign chamber.

The original geometric critical point is also in that chamber.
The real part of the negative unsummed Hessian is positive definite
there, including the two cap blocks. On the convex chamber its
integral along a complex segment is accretive, so the full complex
gradient is injective. The assembled point and the geometric point
therefore coincide. This identifies the branch, without inferring
quantum contribution from geometric existence alone.

The separate
[absolute action calibration](research_three_chain_action_volume_calibration.md)
then gives
\[
 \Xi_m(-2,-2)=
 \sum_{v=0}^{m}\psi(t_v,t_{v+1})
 +\sum_{v=1}^{m}\left(\frac{3it_v^2}{4\pi}-it_v\right)
 +(m-2)i\gamma,\qquad t_0=t_{m+1}=0,
 \tag{16}
\]
where \(\gamma\) is the fixed real constant of that calibration.
In particular
\[
               2\pi\Re\Xi_m(-2,-2)=\operatorname{Vol}(M_m).
 \tag{17}
\]
Here \(M_m\) is the original marked positive partial filling with
both outside ends complete. The complete-edge constants, the actual
boundary action and the original filling terms all occur in (16).
The exponent has not been replaced by the homogeneous value \(2mc\).
The imaginary constant is retained in the phase; it does not alter
(17).

Finally the L40
[ordinary-boundary corner estimate](research_three_chain_fourier_corner_transfer.md#4-a-larger-deleted-corner-for-a-larger-source-domain)
bounds the difference between (13) and the undeleted source
\[
                         v(w_L)^TA_N^m v(w_R)
 \tag{18}
\]
by a polynomial times an exponential of rate
\((2m-1)c+M_\infty+27/200\). The established geometric lower
bound is
\[
 \Re\Xi_m(-2,-2)>
      (2m-1)c+M_\infty+\frac3{25}+\frac1{15}.
\]
Their difference is
\[
                \frac3{25}+\frac1{15}-\frac{27}{200}
                              =\frac{31}{600}>\frac1{20}.
 \tag{19}
\]
This estimate applies to a mixed word with its first and last three
factors undeleted, just as to a fully retained word. It preserves
both parities and the ordinary boundary derivatives. Thus the
undeleted source (18) has the same asymptotic (15).

**Theorem 1.** For every fixed integer \(m\ge10\), the original complete-ended source
satisfies (15), with (17), along all sufficiently large integer levels.
The assertion is at complete ordinary boundary colors, including
their fixed ordinary derivatives; its Fourier-variable preparation
does not enlarge that outside-color scope.
In particular
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|v(-2)^TA_N^m v(-2)|=\operatorname{Vol}(M_m).
 \tag{20}
\]
No uniform starting level as \(m\) grows is asserted. In a literal
marked knot realization, (20) transfers to a Kashaev statement only
after its exact topology and unit or polynomial normalization have
been identified. The carrier relation \(3=\eta_v-2p_v\), primitive
filling data and knot-component test must be retained. The geometric
target in (20) is the marked partial filling with two ends complete;
this scalar-source theorem alone does not identify it with a knot
complement. An abstract cyclic network or different closure is not
substituted.

## 5. Shorter lengths and scope

The one-vertex case is covered separately by the
[nonzero degree-two theorem](research_all_nonzero_degree_two_fillings.md).
The two-vertex case is covered by the original
[internal \((3,3)\) boundary theorem](research_internal_pair_three_full_boundary_packet.md).
The preparation and small-class closure above do not prove the
complete-ended cases \(m=3,4,5,6,7,8,9\). The stronger
[larger-source closure](research_three_larger_source_closure.md)
supplies \(m=6,7,8,9\), leaving \(m=3,4,5\) outside these
arguments. In particular an actual Fourier-ended three-vertex packet
is not the same assertion as its complete-ended closure.

The phase and amplitude germs and fixed derivatives in (15) do not
assert a uniform full-source packet on a fixed complex outside-color
neighborhood, or whole-period decay in those two outside colors. The
internal Fourier-wire envelopes used for propagation are different
estimates. Applying further long fillings at the remaining original
circles would require the appropriate outside-color whole-period
and complex-strip bounds, as well as the original marked component
conditions. Those further boundary hypotheses are not supplied here.

Even after those cases, a theorem for homogeneous three-crossing
chains would not establish cofinite filling assignments on general
fixed templates. Other adjacent short components, degenerate marked
reductions with infinite assignment fibers, and the permitted general
template compositions remain distinct requirements.

The focused checker below verifies the exact length and transpose
bookkeeping, scalar entry and cap comparisons, unit-carrier exponents,
and the corner reserve. It also checks the provenance of the proved
larger-source induction; the analytic contour and volume arguments
remain the cited proofs.

```sh
python3 experiments/check_three_chain_after_entrance.py --precision 192
```
