# Why the mixed-index complement cannot be discarded by absolute values

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The exactly contracted sum has positive sine-product magnitudes and
an explicit quadratic phase. Its real entropy admits useful concavity
estimates. However, an upper bound for that entropy is not an upper
bound at the geometric action. The following obstruction already
occurs for every alternating cycle with at least two pairs of vertices.
It concerns an absolute-value estimate, not the asymptotic value of
the oscillatory sum itself.

## 1. The full finite sum and the two actions

Take the original cyclic contraction
\[
                     C_{k,N}=\operatorname{tr}((A_3A_4)^k),
                           \qquad k\ge2,
 \tag{1}
\]
where \(A_n=JM^n\). This is a specified matrix trace; no knot
interpretation of an arbitrary cyclic graph is asserted. Use the
[exact Fourier contraction](research_mixed_wire_exact_contraction.md)
to expand (1). At every vertex there are two integer leg indices
\(i_v,j_v\in\{0,\ldots,N-1\}\). The exact support restrictions are
\[
                    i_v+j_v<N,\qquad j_v+i_{v+1}<N,
 \tag{2}
\]
with cyclic subscripts. Divide these indices by \(N\), writing
\(s_v=i_v/N\), \(t_v=j_v/N\). Define
\[
                         J(u)=\int_0^u\log(2\sin\pi a)\,da,
                             \qquad 0\le u\le1.
 \tag{3}
\]
The exponential rate of the absolute magnitude of a summand is
\[
 H(\mathbf s,\mathbf t)=
 \sum_v J(s_v+t_v)+\sum_v J(t_v+s_{v+1})
 -\sum_v(2+\mathbf1_{n_v=4})\{J(s_v)+J(t_v)\}.
 \tag{4}
\]
The constant carrier has modulus one and the additional factor
\(N^k\) is polynomial for fixed \(k\). Formula (4) follows from
the sine magnitudes in (17) of the exact contraction note. It does
not use a saddle approximation or a norm estimate.

Let \(\sigma\) denote the selected geometric action for one
alternating pair:
\[
 \sigma=\Re\Phi_3(x_{34},x_{34})+
                   \Re\Phi_4(x_{34},x_{34}).
 \tag{5}
\]
Both phases and their absolute constants are fixed by the
[three-crossing](research_three_vertex_mixed_reference_packet.md) and
[four-crossing](research_power_four_source_packet.md) source theorems.
The periodic reference is stationary for every alternating cycle,
and its action is \(k\sigma\). This identifies a critical action,
not the leading term of the full trace (1).

For a central index region take
\(\mathcal B_k=[1/4,2/5]^{4k}\). Let \(R^{\rm abs}_{k,N}\) be
the sum of the absolute magnitudes of all original contracted
summands whose normalized indices lie outside this region.
All original scalar factors are included.

**Theorem 1.** For every fixed \(k\ge2\),
\[
 \liminf_{N\to\infty}\frac1N\log R^{\rm abs}_{k,N}
                 >k\sigma+\frac1{80}.
 \tag{6}
\]
In particular this complement cannot have an absolute upper bound
at or below the selected geometric rate. The same obstruction applies
if the upper face \(2/5\) is replaced by \(9/20\), because the
configuration used below lies beyond the lower face.

## 2. One explicit configuration for every cycle length

Set the exact rational leg values
\[
                       a=\frac{343}{1000},\qquad
                       b=\frac7{25},\qquad x=\frac6{25}.
 \tag{7}
\]
First put both legs of every three-crossing vertex equal to \(a\),
and both legs of every four-crossing vertex equal to \(b\). The
entropy per alternating pair is
\[
                 h=J(2a)+J(2b)+2J(a+b)-4J(a)-6J(b).
 \tag{8}
\]
Now replace just one leg of a three-crossing vertex by \(x\).
Exactly two adjacent sums and that leg's denominator change. The
loss of entropy is therefore precisely
\[
          c=J(2a)+J(a+b)-2J(a)-J(a+x)-J(x+b)+2J(x).
 \tag{9}
\]
All sums remain strictly between zero and one. Since \(x<1/4\),
the new configuration is outside \(\mathcal B_k\). Its entropy is
\(kh-c\), regardless of the number of other alternating pairs.

Outward evaluation at these rational points and at the validated
algebraic reference proves
\[
               h>1.5369,\qquad c<.0361,\qquad\sigma<1.5126.
 \tag{10}
\]
These inequalities have comfortable strict margins. They use no
numerically optimized real maximum: (7) is an explicit admissible
configuration. Consequently
\[
                 kh-c-k\sigma>.0243k-.0361\ge .0125
                                  \quad(k\ge2).
 \tag{11}
\]
The right side is \(1/80\) at \(k=2\).

For each sufficiently large \(N\), replace the leg values in this
configuration by their lower multiples of \(1/N\). The strict
support margins preserve (2), and the exceptional leg remains below
\(1/4\). This is a literal nonzero summand of the original finite
sum at either parity. Uniform sine-factorial estimates give its
absolute logarithm as
\[
                       N(kh-c)+O_k(\log N).
 \tag{12}
\]
The uniform factorial estimate includes the logarithmic singularity
at the origin; it follows by factoring out that zero, then using
Stirling's formula and a smooth Riemann sum. The sum of absolute
values is at least this one term.
Equations (11)--(12) prove (6). \(\square\)

## 3. Consequence for the proof strategy

The excess in (11) comes from repeating the other, unchanged pairs.
A local loss for one displaced leg has a fixed cost, whereas the
difference between a real absolute entropy and the complex geometric
action accumulates over the remaining vertices. Thus a compactness
or concavity theorem for the real maximum cannot alone justify
discarding the complement at the geometric rate.

The trace (1) retains a quadratic phase. Its summands may cancel,
including in the region isolated by this theorem. A proof may first
sum or integrate the remaining variables while preserving that phase,
or deform an exact representation in which the relevant boundary
terms are controlled. Theorem 1 excludes the earlier step of taking
absolute values of all contracted summands and discarding the index
complement on that basis. It neither disproves the expected geometric
asymptotic nor estimates the signed complement.

Run `python3 experiments/check_mixed_absolute_complement_obstruction.py`.
The checker encloses (10) and verifies the rational support and
all-length comparisons. The written argument passes from that finite
certificate to the actual finite sums and the limit inferior.
