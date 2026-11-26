# The protected collision valuation of the actual nine-cell source

Private written proof, 17 November 2026. The source in [Q] has a
removable normalized singularity at the generic collision of its two
protected vertices. This is proved from its literal finite sum, including
all normalization factors and cyclic carries. No pentagon, published
crossing identification, or projective constancy assertion is used.

## 1. The source and the claimed valuation

Fix odd \(N>2\), a primitive \(N\)-th root \(q\), and \(d=N-1\).
Use the shared roots \(s_{ij}^N=z_i-z_j\), normalizations, charge lift,
and actual boundary tensor \(\mathcal B_\chi\) of [Q]. All finite
indices and charges are taken modulo \(N\). The permitted boundary
charges satisfy \(\sum_m h_m=2\), and the crossing sector satisfies
\(x+y+\zeta+w=1\).

Consider a generic point of \(z_0=z_5\): the five values
\(z_0,z_1,z_2,z_3,z_4\) are pairwise distinct. On a local root cover put
\[
                 h=s_{05},\qquad z_5=z_0-h^N.                 \tag{1}
\]
All other edge roots are nonzero and holomorphic in \(h^N\), with
their original branches retained. The other five decorations may vary
in a sufficiently small neighborhood throughout the argument.

**Theorem.** On every such compatible local branch, every boundary
entry of the actual source has the divisibility
\[
                         \mathcal B_\chi\in h^d\mathcal O.     \tag{2}
\]
Consequently every entry of the recovered four-index tensor
\(\mathcal R^\chi\) in [Q, (18)] extends holomorphically across this
generic protected divisor. The statement includes every permitted
\(\mathbf h,\chi\) and both cyclic endpoint indices. It does not assert
that the order in (2) is exactly \(d\), or that the extension is nonzero.

Here \(\mathcal O\) denotes holomorphic functions on the local cover,
including the continued normalization square roots. We first verify
that these square roots and their finite scalar sums introduce no
unaccounted pole.

## 2. All tetrahedral scalar factors at this divisor

The five cells not containing both \(0,5\) remain on their ordinary
regular loci. For a collar cell \(T=0ab5\), use [B]'s scalar variables
\[
 (P,Q,R,B,C,H)=(s_{0a},s_{ab},s_{b5},s_{0b},s_{a5},h).
\]
All five variables other than \(H\) are nonzero at \(h=0\).
The exact squared prefactor is
\[
 \kappa_*^2=
 \frac{B^NQ^N(H-C)}{N^2(B-Q)(H-R)(C-R)}.                       \tag{3}
\]
Every factor in (3) is a unit at \(h=0\). For example
\(B^N-Q^N=P^N\ne0\) and \(C^N-R^N=Q^N\ne0\), so
\(B-Q,C-R\ne0\). Thus both compatible choices of \(\kappa_*\)
continue holomorphically and are units.

The scalar sums are
\[
 \rho=\kappa_* f(R/H,R/(qC)\mid BC/(HQ)),\qquad
 \bar\rho=\kappa_* f(R/C,R/(qH)\mid HQ/(BC)).                  \tag{4}
\]
The \(k\)-th summand of the first \(f\) is exactly
\[
 \left(\frac{BC}{Q}\right)^k
 \prod_{j=1}^k\frac{1-(R/C)q^{j-1}}{H-Rq^j},
                  \qquad 0\le k<N.                           \tag{5}
\]
The \(k\)-th summand of the second is
\[
 \left(\frac{Q}{BC}\right)^k
 \prod_{j=1}^k\frac{H-Rq^{j-1}}{1-(R/C)q^j}.                  \tag{6}
\]
These finite expressions are holomorphic at \(H=0\); all their
denominators are units there. The independently proved normalization
product [B, (12)] is
\[
                     \rho\bar\rho=\frac{(PR)^N}{N(BC-HQ)}.    \tag{7}
\]
It is a unit at \(H=0\). Equations (5),(6), followed by (7), prove
that both scalar sums are units. The product alone would not have
excluded a pole in one factor and a zero in the other.

In particular the full source normalization
\[
\begin{split}
\mathfrak n={}&(s_{12}s_{23}s_{34}s_{14})^{-d}
\rho_{1234}\rho_{1245}\rho_{2345}\rho_{0123}\rho_{0134}\\
&\hspace{12mm}\cdot\bar\rho_{0125}\bar\rho_{0235}
\bar\rho_{0345}\rho_{0145}
\end{split}                                                   \tag{8}
\]
is holomorphic and nonzero near this generic divisor. No vertex,
edge, or scalar factor of the actual source has been discarded.

## 3. The last finite sum and its cyclic carries

For a collar \(0ab5\), put
\[
 \alpha_{ab}=\frac{s_{ab}}{s_{0b}s_{a5}},\qquad
 \beta_{ab}=\frac{s_{0a}s_{b5}}{s_{0b}s_{a5}}.
\]
These functions are holomorphic in \(h^N\), and satisfy exactly
\[
 \beta_{ab}^{\,N}=1-h^N\alpha_{ab}^{\,N},\qquad
                  \beta_{14}=\beta_{12}\beta_{23}\beta_{34}.  \tag{9}
\]
The second equality uses the same shared edge roots, not independently
chosen roots of the four ratios. The literal products are
\[
 W_{0ab5}(n)=\beta_{ab}^{[n]}
       \prod_{j=1}^{[n]}(1-h\alpha_{ab}q^j)^{-1},\qquad
 \bar W_{0ab5}(n)^{-1}=\beta_{ab}^{-[n]}
       \prod_{j=1}^{[n]}(1-h\alpha_{ab}q^{j-1}).               \tag{10}
\]

In [Q, (16),(17)], rename its last summation index \(\ell\).
For each fixed choice of the other five indices, its entire
\(\ell\)-dependent factor is precisely
\[
 \sum_{\ell=0}^{N-1}q^\ell
 \frac{W_{0145}(\ell)}
 {\bar W_{0125}(\ell+A_1)\bar W_{0235}(\ell+A_2)
                           \bar W_{0345}(\ell+A_3)},           \tag{11}
\]
where
\[
 A_1=1-k_1+r+s,\quad A_2=2-k_1-k_2+u+v+s,\quad
 A_3=k_4+t+v.                                                 \tag{12}
\]
All remaining factors are independent of \(\ell\) and holomorphic
at \(h=0\). This includes their original phase and the normalization
(8). Off the actual boundary support \(\sum k_m=2\), the source is
identically zero already.

Work modulo \(h^N\). By (9), replacing a residue \([\ell+A_j]\)
by its integer representative changes its \(\beta\) power only by
a factor congruent to one. Also \(\alpha_{ab}(h)\equiv\alpha_{ab}(0)\)
and \(\beta_{ab}(h)\equiv\beta_{ab}(0)\) modulo \(h^N\).
Thus (9) cancels all geometric \(\ell\) dependence in (11), leaving
a constant nonzero factor and the four product corrections in (10).
This step retains the endpoint carry because its first possible
correction has order \(h^N\).

For \(1\le j<N\), the coefficient of \(h^j\) in the formal logarithm
of either product correction is a scalar multiple of
\[
 \sum_{v=1}^{[\ell+A]}q^{j(v+e)}
       =q^{j(1+e)}\frac{1-q^{jA}(q^\ell)^j}{1-q^j},
                            \qquad e=0\text{ or }-1.          \tag{13}
\]
The sign depends on whether the product is inverted. Every denominator
in (13) is nonzero, including at composite levels. Hence the coefficient
of \(h^k\), for \(k<N\), in the product of all four corrections is a
polynomial \(P_k(X)\) in \(X=q^\ell\) of degree at most \(k\).
Indeed each logarithmic term has \(X\)-degree at most its \(h\)-degree,
and multiplication and formal exponentiation preserve that inequality.
Only truncated formal logarithms of series with constant term one
are used; no infinite product at a root of unity is asserted.

For \(0\le k\le N-2\), therefore,
\[
                \sum_{\ell=0}^{N-1}q^\ell P_k(q^\ell)=0,      \tag{14}
\]
since the powers being summed range from \(1\) to \(k+1<N\).
Thus (11) is divisible by \(h^{N-1}\). Summing the other five finite
indices preserves that valuation. This proves (2) in the canonical
sector. The exact sector transport [Q, (17a),(17b)] multiplies each
boundary entry by a root-of-unity phase depending only on the boundary
indices and charges; it is independent of \(\ell\) and the decorations.
It proves the same conclusion for every allowed sector.

## 4. The actual inverse adapter and the remaining scope

The recovered array is, literally,
\[
 \mathcal R^\chi_{\mathbf i}
 =\frac{1}{h^dN^4}\sum_{\mathbf k} b_\chi(\mathbf k)
       \prod_{m=1}^4\frac{q^{-i_mk_m}}{f_m(k_m)},\qquad
 f_m(k)=s_{0m}^{[k-1]}s_{m5}^{[-k]}.                           \tag{15}
\]
Here \(b_\chi\) is the actual boundary tensor as a function of its
four differences, extended by zero off its support. At the generic
collision in (1), every \(s_{0m},s_{m5}\) is nonzero. Thus every
\(f_m(k)\) and its inverse are holomorphic units, including \(k=0,1\).
Apply (2) term by term to (15): its only displayed singular power,
\(h^{-d}\), is removable. All original Fourier factors and \(N^4\)
remain unchanged.

The extension is joint in the spectator decorations on the local
cover, so its fixed-order derivatives there are holomorphic as well.
No uniform large-\(N\) bound or off-root quantum derivative is claimed.
This removes the generic \(05\) divisor only. Other collision divisors,
their intersections, decoration independence, the full crossing-array
identification, and any selected geometric contribution remain outside
the theorem. No collision term or relative source current is deleted
by calling the normalized singularity removable.

## Complete direct sources

- [Q] [Literal nine-cell boundary source](research_nine_tetrahedron_boundary_source_reduction.md),
  SHA256 `5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c`.
- [B] [Literal charged tetrahedron bubble](research_literal_charged_tetrahedron_bubble.md),
  SHA256 `1dfe35f26137572235b1c3af66dcf410e0af758836baddaa8dd6d958c0f61d9b`.

Both complete texts were read and the used finite identities checked.
No mathematical programs, numerical experiments, or published
nine-cell contraction were used.
