# Two open boundaries of a same-sign two-crossing chain

The same-sign chain identity has a useful tensor form. Both outside
boundaries remain open: the reduced object is a degree-two filled
vertex, with one boundary crossing on each side. It is not a terminal
source. This distinction determines which existing estimates apply.

The algebraic identity and the full two-boundary asymptotic below
hold for every fixed positive chain length. The missing short
internal powers are supplied by
[the degree-two filling theorem](research_all_nonzero_degree_two_fillings.md).
Both boundary crossing factors are canonically reduced with their
full Hermite data.

## 1. The exact tensor

Let \(D=N-1\), \(q=e^{\pi i/N}\), and
\(\kappa_N=q^{D^2/2}\), with the displayed logarithm of \(q\).
Use the original Newton algebra
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
\]
Let \(M\) be multiplication by the original crossing \(R\), and
\(J\) Newton coefficient reversal. For a signed integer \(n\),
the full two-boundary source of one degree-two vertex is
\[
 P_{2,n,N}(u,v)=
 \phi_N^{(t)}[R^nK_N(t,u)K_N(t,v)].
 \tag{1}
\]
Its coefficient matrix in the basis \(e_i(z)e_j(w)\) is
\[
                         A_n=JM^n=A_n^T.
 \tag{2}
\]
This follows directly from the Frobenius pairing; it includes
the first normals at every repeated spectral root.

For \(k\ge1\) and \(\sigma=\pm1\), let \(C_{k,\sigma,N}\)
be the full source obtained from a path of \(k\) internal
vertices of power \(2\sigma\), with an outgoing edge at
each end. The shared original edge sums equal Newton
indices. Thus its coefficient matrix is
\[
                          \mathbf C_{k,\sigma}=(JM^{2\sigma})^k.
 \tag{3}
\]
In particular, (3) is not a pendant coefficient column.

**Proposition 1.** At every level and for every \(k\ge1\),
\[
 \boxed{\displaystyle
 (JM^{2\sigma})^k
 =\kappa_N^{\sigma(k+1)}
       M^{-\sigma}(JM^{-\sigma(k+1)})(M^{-\sigma})^T.}
 \tag{4}
\]
Equivalently, in \(\mathcal A_N\otimes\mathcal A_N\),
\[
 C_{k,\sigma,N}
 =\kappa_N^{\sigma(k+1)}
          (R^{-\sigma}\otimes R^{-\sigma})
                    P_{2,-\sigma(k+1),N}.
 \tag{5}
\]
The right side is canonically reduced in both boundary variables
when interpreted as an ordinary polynomial.

*Proof.* The original identities are
\[
 J^2=I,\qquad JM^\sigma J
       =\kappa_N^\sigma M^{-\sigma}JM^{-\sigma},
       \qquad (M^r)^T=JM^rJ.
 \tag{6}
\]
The all-length operator identity in
[the marked chain reduction](research_repeated_two_crossing_chain_reduction.md),
equation (3), is
\[
 (JM^{2\sigma})^kJ
  =\kappa_N^{\sigma(k+1)}
        M^{-\sigma}JM^{-\sigma(k+1)}JM^{-\sigma}.
\]
Multiply on the right by \(J\) and use the last identity in
(6). This proves (4). Multiplication by \(R^{-\sigma}\)
in the first tensor variable left-multiplies its coefficient
matrix by \(M^{-\sigma}\); multiplication in the second
right-multiplies it by \((M^{-\sigma})^T\). This is precisely
(5). All identities are in the full algebra, not its
semisimple quotient. \(\square\)

The transpose in (4) is an ordinary transpose. It is not a
conjugate transpose. Omitting it would give a different tensor.
Nor does (5) give equality with the unreduced ordinary product
at arbitrary complex boundary values. The estimates in the
next section justify that comparison at exponential accuracy.

## 2. Boundary multiplication with the other parameters retained

The one-variable
[boundary multiplication theorem](research_boundary_crossing_packet_preservation.md)
extends to a joint source. We give the parameter argument
because preserving only the complete value of the other
boundary would not be enough for (5).

**Proposition 2.** Suppose \(F_N(u,v)\) has spectral degree at
most \(D\) in each variable and is separately even. Suppose
its full polynomial satisfies
\[
 |F_N(x+iy,s+it)|\le CN^d
 e^{N\{M-c(1-\cos x)-c(1-\cos s)+B(y^2+t^2)\}}
 \tag{7}
\]
on a fixed whole-period product strip, with \(c>0\), and
has a full local packet
\[
 F_N(u,v)=\epsilon_N N^\alpha A(u,v)e^{NS(u,v)}
                                  (1+O(N^{-1})),
 \tag{8}
\]
on a fixed bidisk. The amplitude is holomorphic and
nonzero, the normalized error is holomorphic, the phase is
separately even, \(\Re S(0,0)=M\), and its real Hessian at
zero is negative definite.

For fixed signed integers \(r,s\), canonical multiplication
in both variables has the full local expansion
\[
\begin{split}
 &\operatorname{can}_{u,v}
       [(R^r\otimes R^s)F_N](u,v)\\
 &\quad=\epsilon_N C_{N,r}C_{N,s}N^\alpha A(u,v)
  \exp N\left\{S(u,v)+\frac{i}{4\pi}(ru^2+sv^2)\right\}
                              (1+O(N^{-1})),
 \qquad C_{N,r}=e^{\pi i rD^2/(4N)}.
\end{split}
 \tag{9}
\]
It also has a bound of the form (7), on a fixed possibly
smaller product strip, with positive angular coefficients.
All assertions include both parities and all tensor
Hermite jets, including the mixed first normal.

For a family with common constants in (7), a common full
expansion and zero-free amplitude bidisk in (8), common
normalized phase bounds and a common positive real
curvature bound, the output constants can be common for
a fixed finite set of pairs \((r,s)\). Prefactors and
starting levels may depend on the member.

*Proof.* First multiply in \(u\) only. Fix a complex
parameter \(v=s+it\) in the input strip, and put
\[
                     M(v)=M-c(1-\cos s)+Bt^2.
\]
The exact one-variable Fourier-cutoff proof applies with
this baseline. Every derivative estimate, endpoint bound
and Fourier-tail estimate in that proof is uniform in
this parameter, since (7) supplies the same strip constants.
Thus, for the full Hermite interpolant \(P_N\),
\[
 |P_N(u,v)-C_{N,r}e^{irNu^2/(4\pi)}F_N(u,v)|
        \le C_rN^{d_r}e^{N(M(v)-\delta)}
 \tag{10}
\]
for real \(u\) and all these complex parameters, with one
\(\delta>0\). The physical jets agree exactly before any
estimate. The exact Fourier folding weights retain all
aliases and the odd zero mode.

For each fixed complex \(v\), apply the same half-disk
two-constants argument to the analytic difference in
(10). The crude upper-half-disk bound has baseline
\(M(v)\) and common constants, so it gives
\[
 |P_N(u,v)-C_{N,r}e^{irNu^2/(4\pi)}F_N(u,v)|
        \le C_r'N^{d_r'}e^{N(M(v)-\delta/2)}
 \tag{11}
\]
on a fixed small complex \(u\)-disk. Decrease the outside
\(v\)-disk so \(B|\Im v|^2<\delta/8\), and then decrease
the joint disk so the real part of
\(S(u,v)+iru^2/(4\pi)\) is at least \(M-\delta/8\).
Equation (11) is exponentially smaller than the nonzero
packet (8). This proves its full holomorphic two-parameter
expansion after the first multiplication.

On the real torus the chirp has modulus one. Combining
(10) and (7) gives a strict angular loss in both variables:
the loss in \(v\) factors out, and the \(u\) loss can be
decreased to \(\min(c,\delta/2)>0\). The new phase adds
only an imaginary diagonal quadratic term, so its real
Hessian at zero is unchanged.

For clarity the joint strip is recovered as follows. Near
the origin the local packet, negative real Hessian and
Young's inequality give
\[
 \Re S_{\rm new}(x+iy,s+it)
        \le M-a(x^2+s^2)+B_1(y^2+t^2).
 \tag{12}
\]
Outside a smaller real neighborhood of the origin, cover
the compact spectral square by finitely many products of
real intervals, enlarged slightly so their real angular
gap persists. At least one coordinate is away from its
complete endpoint. The separate degrees are at most \(D\).
Applying the interval Chebyshev/Bernstein--Walsh bound in
both variables preserves a fixed gap on a sufficiently
thin product strip: the two Green-function costs tend
uniformly to zero on these fixed interval products.
Combining this with (12) gives a bound of the form (7).
This argument also covers points where one angle is
small and the other is large.

Repeat the same argument in \(v\), now with the already
controlled first-multiplied source. The two canonical
multiplication operators commute because they act in
different tensor factors. Their carrier factors and
quadratic phases multiply and add exactly, proving (9).
The common-family assertion follows from the same uniform
choices; no common lower bound on amplitude size is needed.
The mixed normal is preserved by the commuting full
one-variable Hermite interpolants. \(\square\)

## 3. The full chain packet at every fixed length

Suppose a degree-two power \(n\) has the proved full packet
\[
 P_{2,n,N}(u,v)=\epsilon_{n,N}N^{-3/2}
                 A_n(u,v)e^{NS_n(u,v)}(1+O_n(N^{-1})),
 \tag{13}
\]
with its whole two-boundary Gaussian strip and nonzero
amplitude. Apply Proposition 2 to (5), using
\(n=-\sigma(k+1)\) and \(r=s=-\sigma\). The actual chain
polynomial has
\[
\begin{split}
 C_{k,\sigma,N}(u,v)
   ={}&\kappa_N^{\sigma k}\epsilon_{-\sigma(k+1),N}
           N^{-3/2}A_{-\sigma(k+1)}(u,v)\\
    &\times
       \exp N\left\{S_{-\sigma(k+1)}(u,v)
                   -\frac{\sigma i}{4\pi}(u^2+v^2)\right\}
                              (1+O_k(N^{-1})).
\end{split}
 \tag{14}
\]
Indeed \(\kappa_N^{\sigma(k+1)}C_{N,-\sigma}^2
=\kappa_N^{\sigma k}\). The real boundary Hessian remains
negative definite, and a strict whole two-boundary strip
bound follows from Proposition 2.

The required hypotheses (13) are now established for every
fixed \(k\ge1\):

* \(k=1\): use
  [the degree-two powers \(2,-2\) theorem](research_degree_two_power_two_boundary_theorem.md)
  and its recorded phase convention.
* \(2\le k\le30\): the reduced power has magnitude
  \(3,\ldots,31\). The complete source, including its two
  free boundaries, is proved in
  [the degree-two filling theorem](research_all_nonzero_degree_two_fillings.md)
  by the scaled trace-first contours and their nineteen
  outward-certified surfaces.
* \(k\ge31\): then \(|n|=k+1\ge32\), and \(d=2\) satisfies
  \(d^2+n^2\ge\max(1024,128d)\) in
  [the degree-and-power theorem](research_high_degree_short_internal_vertex.md).

For both ranges \(k\ge2\) the source theorem takes
\(\epsilon_{n,N}=C_{N,n}\). The complete unit in (14)
can therefore also be written \(C_{N,\sigma(k-1)}\).
For \(n=\pm2\) the direct two-index source theorem has
\(\epsilon_{n,N}=1\) with its direct phase, or the
equivalent calibrated geometric phase has
\(\epsilon_{n,N}=e^{\operatorname{sgn}(n)i\pi N/2}\).
Either convention may be used in (14), but its unit
and phase must be taken together. No principal fractional
power of a numerical unit replaces the stated \(q\)-logarithm.

Each fixed length has a full bidisk and
whole-boundary strip. The statement so far does not require
their widths to be uniform as \(k\) varies. Such uniformity
requires checking the large-\(|n|\) two-boundary family,
not merely the terminal family.

## 4. Markings and the source estimate used by the reduction

The geometric reduction is the all-length marked identity
in Section 3 of
[the chain reduction note](research_repeated_two_crossing_chain_reduction.md).
For an arbitrary attached tangle, the proper physical
rotation indexed by \(k\bmod4\) is retained:
\[
 \rho_k=\tau,\rho,\mathrm{id},K
                     \quad\text{for }k=0,1,2,3\pmod4.
 \tag{15}
\]
There are boundary crossing shifts on both sides.
Only a pendant through cap permits its stabilizer to
remove the rotation. An open two-boundary tensor cannot
be used to silently erase it. When the chain is inserted
in a larger marked diagram, transport this rotation,
the boundary disk frames and both crossing shifts exactly
as in that tangle identity. Equation (4) alone is not
a replacement proof of the marked isotopy.

For \(k=2,\ldots,30\), the reduced vertex has power magnitude
\(3,\ldots,31\), and its degree is two. It is essential to
use the new two-boundary theorem here. The terminal theorems
for those magnitudes estimate
\[
 H_{n,N}(u)=\phi_N^{(t)}[R^nK_N(t,u)],
\]
whereas (1) contains a second complete kernel and a
different joint stationary problem. Their terminal
contour bounds do not estimate that extra factor on the
entire deformed contour. Positive or nonzero data at one
boundary value likewise would not suffice.

The relevant joint phase before eliminating the wire
variables is
\[
 b(x,t)+b(x,u)+b(y,t)+b(y,v)
                    +\frac{int^2}{4\pi}-it.
 \tag{16}
\]
The two wire variables interact through the same original
trace angle. The new proof first takes the exact angular
trace, then applies the one-sided summation identity in
each wire on that contour. The full phase at complete
parents is the average of two copies of the scaled phase
\(2[b(x,t)+b(x,0)]+int^2/(4\pi)-it\). Each wire penalty
is doubled in that scaled phase; the angular charge stays
once. The certified two-variable inequalities therefore
bound every combination of wire endpoints and aliases.
The three-dimensional Gaussian and the exact factorial
shifts give precisely (13), with exponent \(N^{-3/2}\).

This note proves a full boundary reduction and its
analytic consequence for every fixed length. Any use in a
filled-knot volume theorem must also carry the physical
rotations and the original marked boundary maps just
described.

## 5. Finite normalization check

The standalone script
[check_internal_two_crossing_chain.py](../experiments/check_internal_two_crossing_chain.py)
checks (4) with the original crossing matrix, both signs
and both level parities. It compares the entire coefficient
matrix, and its values and first spectral derivatives in
both boundary variables, including the mixed derivative.
It also records why the unreduced ordinary product in
(5) is not the canonical boundary polynomial.

~~~sh
python3 experiments/check_internal_two_crossing_chain.py \
  --precision 120 \
  --output repro/results/research-internal-two-crossing-chain.json
~~~

The [saved record](../repro/results/research-internal-two-crossing-chain.json)
contains 144 full-matrix cases at \(N=2,\ldots,10\), both signs,
and lengths \(1,2,3,4,7,8,31,32\). It also contains 1,728
boundary jet comparisons, including mixed first normals.
All passed at 120 decimal digits; the largest relative
residual was below \(1.99\cdot10^{-111}\). At one recorded
off-spectrum pair the unreduced ordinary product differs
from the canonical polynomial by relative size greater
than \(0.06\), illustrating the distinction in Proposition 1.

These are finite algebraic diagnostics. The asymptotic
estimates come from the source theorems and Proposition 2,
not from these finite comparisons.
