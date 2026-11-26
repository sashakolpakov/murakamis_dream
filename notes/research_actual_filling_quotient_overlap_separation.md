# Actual filling separation and the positive quotient minimum

Private written proof, 18 November 2026.

The explicit positive quotient minimum preserves the original filled
period. It does not make the original exterior nearly invariant under
the co-source operators. A larger period at another fixed filling
forces an exponentially small overlap with the target period line.
This statement applies to arbitrary coupled exterior sources, with
every Hermite normal retained.

An already established, source-exact normalization packet gives an
unconditional application at every level. Its target closing is a
unit, but its overlap fraction in the new metric tends to zero
exponentially. The packet inserts into any nonzero exterior. This
does not disprove a geometric lower bound for the quotient minimum:
it rules out deriving that bound from automatic near-invariance of
the raw source.

The three complete proof directs are K, the canonical Hermite
splitting; C, the arbitrary-power source compiler; and G, the actual
Fourier--Hermite Gram and normalization packet. Exact pins appear
at the end. No numerical calculation is used.

## 1. The source class and the metric

Use the full physical algebra and its prescribed circle basis:
\[
 \mathcal H_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 L_j=(-1)^{j-1}U_{j-1}(z/2),\quad 1\le j\le N.
 \tag{1}
\]
The basis is orthonormal for the norm denoted by \(\|\cdot\|_2\).
This is not the circle coefficient \(\ell^1\) norm.
The actual crossing \(R\), including its Cartan phase, is a unit
of this full algebra. The original row obeys
\[
 \phi(L_j)=N^2\mathbf1_{j=N},\qquad
 \phi_{\boldsymbol n}
       =\bigotimes_{i=1}^r\bigl[f\mapsto\phi(R^{n_i}f)\bigr].
 \tag{2}
\]

Let \(H_N\in\mathcal H_N^{\otimes r}\) be the class of an original
exterior after a specified fixed short partial assignment, with the
remaining \(r\) slots open. It may be arbitrarily coupled. C proves
that the actual finite contractions and signed powers provide this
class, preserving all double-root normals and the odd simple value.
An unreduced ordinary boundary polynomial can have larger degree;
its class is used here only for the exact finite functional. No
claim about its individual Fourier-charge integrals follows from
this reduction.

For a fixed signed tuple \(\boldsymbol n\), put
\[
 T_{\boldsymbol n}=\bigotimes_i M_{R^{n_i}},\qquad
 \|H\|_{\boldsymbol n}=\|T_{\boldsymbol n}H\|_2.
 \tag{3}
\]
Use K's operators \(K_i=\widetilde K_{n_i}\) and orthogonal
projections \(P_i\) in their respective slots, and set
\(P_{\boldsymbol n}=\prod_iP_i\). Their known normalization is
\[
 \|P_{\boldsymbol n}H\|_{\boldsymbol n}
              =\frac{|\phi_{\boldsymbol n}(H)|}{N^{2r}}.
 \tag{4}
\]
When \(H\ne0\), define its target overlap fraction by
\[
 \rho_{\boldsymbol n}(H)=
 \frac{\|P_{\boldsymbol n}H\|_{\boldsymbol n}^2}
      {\|H\|_{\boldsymbol n}^2}.
 \tag{5}
\]
All additional original external lines remain outside (2).
Common nonzero scalar factors cancel from (5) and from the
period ratios below; their normalization is not changed.

## 2. Two fixed fillings of the same exterior

For an integer tuple \(\boldsymbol d\), define the explicit bound
\[
 B_{\boldsymbol d,N}
       =6^rN^{5r/2}\prod_{i=1}^r(1+|d_i|/2).
 \tag{6}
\]
K's full-Hermite multiplication estimate gives
\[
 \|T_{\boldsymbol d}\|_{2\to2}\le B_{\boldsymbol d,N}.
 \tag{7}
\]
The estimate is polynomial for every fixed tuple, including negative
powers. It uses the entire crossing, not only its distinct nodal values.

**Proposition 1.** If
\(\phi_{\boldsymbol m}(H)\ne0\), then
\[
 \boxed{\quad
 \rho_{\boldsymbol n}(H)
 \le B_{\boldsymbol m-\boldsymbol n,N}^{\,2}
       \left|\frac{\phi_{\boldsymbol n}(H)}
                    {\phi_{\boldsymbol m}(H)}\right|^2 .
 \quad}
 \tag{8}
\]

**Proof.** In the tensor orthonormal circle basis, the row
\(\phi^{\otimes r}\) has norm \(N^{2r}\). Multiplication in the
different slots and powers of the same \(R\) commute, so
\[
 \begin{split}
 |\phi_{\boldsymbol m}(H)|
 &=|\phi^{\otimes r}
           (T_{\boldsymbol m-\boldsymbol n}T_{\boldsymbol n}H)|\\
 &\le N^{2r}B_{\boldsymbol m-\boldsymbol n,N}
                               \|H\|_{\boldsymbol n}.
 \end{split}
 \tag{9}
\]
Combine this with (4)--(5). No positivity of the source
coefficients and no factorization of \(H\) were used. \(\square\)

For example, if two original fixed fillings satisfy
\[
 \limsup_N N^{-1}\log|\phi_{\boldsymbol n}(H_N)|\le v,
 \qquad
 \liminf_N N^{-1}\log|\phi_{\boldsymbol m}(H_N)|\ge w>v,
 \tag{10}
\]
then, with \(\log0=-\infty\),
\[
 \limsup_N N^{-1}\log\rho_{\boldsymbol n}(H_N)
                                      \le-2(w-v).
 \tag{11}
\]
This is an upper bound, not an equality. A matching whole-source
norm rate would be needed for equality. The fixed-power assumption
is essential to treating (6) as subexponential.

The metrics for any two fixed tuples are polynomially equivalent,
by applying (7) in both directions. Consequently all these raw
norms have the same exponential rate when that rate exists.
They cannot simultaneously be sharply concentrated on period
lines whose actual filled scalars have different exponential rates.

## 3. The residual that almost-invariance would have to control

The least nonzero eigenvalue of the single-slot \(K_0\) is exactly
\[
 \lambda_{*,N}
  =\frac{\sin((N-1)\pi/N)}{(N-1)\pi/N}
  =\frac{N\sin(\pi/N)}{(N-1)\pi}>0.
 \tag{12}
\]
Indeed \(\sin x/x\) decreases on \((0,\pi)\), as proved in K.
Its asymptotic size is \(N^{-1}\).

Expand \(T_{\boldsymbol n}H\) in the tensor circle basis.
Any basis vector outside the all-\(L_N\) line has at least one
slot with eigenvalue at least \(\lambda_{*,N}\). Therefore
\[
 \boxed{\quad
 \sum_i\|K_iH\|_{\boldsymbol n}^2
 \ge\lambda_{*,N}^2
         \|H-P_{\boldsymbol n}H\|_{\boldsymbol n}^2
 =\lambda_{*,N}^2(1-\rho_{\boldsymbol n}(H))
                                      \|H\|_{\boldsymbol n}^2 .
 \quad}
 \tag{13}
\]
Thus (11) rules out, for any fixed \(0\le\delta<1\), the estimate
\[
 \sum_i\|K_iH_N\|_{\boldsymbol n}^2
 \le\delta^2\lambda_{*,N}^2\|H_N\|_{\boldsymbol n}^2
 \tag{14}
\]
at all sufficiently large levels. A residual of order \(N^{-1}\)
relative to the source norm is not by itself enough: it must be
small relative to the actual gap with the required constant.

For clarity the positive quotient minimum is still exact:
\[
 \inf_{V_1,\ldots,V_r}
 \left\|H-\sum_iK_iV_i\right\|_{\boldsymbol n}^2
       =\|P_{\boldsymbol n}H\|_{\boldsymbol n}^2
       =\frac{|\phi_{\boldsymbol n}(H)|^2}{N^{4r}}.
 \tag{15}
\]
Here the sum of the images is the orthogonal complement of the
period line. One direct verification sets
\[
 E_i=\left(\prod_{j<i}P_j\right)(I-P_i).
 \]
These are mutually orthogonal, sum to \(I-P_{\boldsymbol n}\),
and \(E_iH=K_iG_{n_i}E_iH\) by K. Orthogonal projection then
proves (15). The minimizing residual is unique; the list of
co-source potentials need not be. This is a vector-space
statement, not an algebra quotient.

Equations (8) and (13) concern the actual raw representative.
They do not obstruct a geometric analysis of the minimized
quantity in (15), or of a separately constructed co-source
subtraction that retains the correct analytic currents.

## 4. An unconditional application to the original normalization packet

G, §§3--4, retains one actual open auxiliary slot and defines
its full mixed-circle exterior by
\[
 A_j=\ell\,R_2^2L_{j+1}(\Omega_{12})R_1R_2p,
                       \qquad 0\le j<N.
 \tag{16}
\]
All displayed turns, physical crossings, pivots and common
framing phases are the original ones.

There is a specific actual Frobenius boundary \(H_N\) for this
slot, characterized by
\[
 \phi(fH_N)=\ell\,R_2^2f(\Omega_{12})R_1R_2p
                         \qquad(f\in\mathcal H_N).
 \tag{17}
\]
This is not a choice made from the unknown target period.
For instance, C's exact identity kernel and its Newton dual
basis give
\[
 H_N=\sum_{j=0}^{N-1}
       \bigl(\ell R_2^2e_j(\Omega_{12})R_1R_2p\bigr)e_{N-1-j},
 \tag{18}
\]
because \(\phi(e_i e_j)=\mathbf1_{i+j=N-1}\).
Thus (18) is the ordinary original boundary contraction.

G proves the two whole-source identities
\[
 \phi_0(H_N)=\kappa^2,\qquad
 \phi_{-2}(H_N)=Z_N,\qquad
 Z_N=\sum_{a=0}^{N-1}|(Q;Q)_a|^2,\quad
 Q=e^{2\pi i/N}.
 \tag{19}
\]
In particular \(H_N\ne0\) at every level. Using
\(B_{-2,N}=12N^{5/2}\), Proposition 1 gives
\[
                    \rho_0(H_N)\le\frac{144N^5}{Z_N^2}.
 \tag{20}
\]

Here is an elementary exponential estimate needing no known
knot asymptotic. Put
\[
 S_a=\prod_{k=1}^a2\sin(\pi k/N),\qquad a=\lfloor5N/6\rfloor.
 \]
The factorization of \((z^N-1)/(z-1)\) at \(z=1\), followed by
absolute values, gives \(S_{N-1}=N\). Every factor in
\(S_{N-1}/S_a\) is at most one. Among them the indices
\(\lceil11N/12\rceil\le k\le N-1\) have factors at most
\(\pi/6<2/3\); there are at least \(N/12-1\) such indices.
The same inequality is valid if this lower count is negative.
Consequently
\[
 S_a\ge N(3/2)^{N/12-1},\qquad
 Z_N\ge S_a^2\ge N^2(3/2)^{N/6-2}.
 \tag{21}
\]
Combining (20)--(21) proves the all-level explicit bound
\[
 \boxed{\quad
 \rho_0(H_N)\le
       144(3/2)^4\,N(3/2)^{-N/3}.
 \quad}
 \tag{22}
\]
In particular the normalized squared \(K_0\) residual in (13)
is at least
\[
 \frac{\|K_0H_N\|_2^2}{\|H_N\|_2^2}
 \ge\lambda_{*,N}^2
       \left[1-144(3/2)^4N(3/2)^{-N/3}\right].
 \tag{23}
\]
The right side can be negative at small levels without affecting
the inequality. It approaches the gap scale from below.

G further proves that the target zero-filled tangle in (16)
is the identity strand up to its retained unit framing factor,
and every mixed-circle entry is scalar on the original complete
head. Inserting this already specified normalization packet into
any exterior with nonzero original cut scalar therefore multiplies
\(H_N\) by that same scalar. Its overlap fraction (22) is unchanged.
No physical exterior is replaced by a positive model.

This is the previously established normalization insertion, not a
new knot example or a claim that every reduced long-filling source
has this form. It proves that exact source compilation, full normal
data and polynomially conditioned co-source splitting do not
automatically imply raw near-invariance, even for an insertion that
does not change the target knot.

## 5. Endpoint and positivity qualifications

The argument above uses exact filled periods of the same class,
so it is unaffected by the degree of the unreduced boundary
polynomial. There is a useful but more restricted endpoint bound.
For the canonical representative, \(L_j(-2)=j\), so evaluation
has norm
\[
 e_N=\left(\sum_{j=1}^Nj^2\right)^{1/2}.
 \]
Hence
\[
 \rho_{\boldsymbol n}(H)
 \le
 \frac{e_N^{2r}B_{-\boldsymbol n,N}^2
             |\phi_{\boldsymbol n}(H)|^2}
      {N^{4r}|H_{\rm can}(-2,\ldots,-2)|^2}
 \tag{24}
\]
whenever that denominator is nonzero. This cannot be combined
silently with a bound for an unreduced boundary value. At even
levels \(\chi_N(-2)=4\), so that value is not class-invariant.
At odd levels \(\chi_N(-2)=0\), and evaluation agrees with the
unreduced value. A matching norm upper rate is still required
before replacing a limsup consequence by an equality.

The positive quantity (15) is well defined and removes the
excess directions of the raw norm. Its explicit metric and
relations do not yet provide a source-dependent lower estimate.
The actual short-word compiler retains signed quadratic crossing
phases and normal data; it supplies no general phase alignment or
almost-invariance estimate. Positivity available for specially
reflected whole words is not presumed for arbitrary fixed short
partial fillings. No finite-exception case, physical cycle
coefficient, or geometric volume lower bound is added here.

## Complete proof-source pins

* K: notes/research_canonical_hermite_filling_kernel_split.md,
  SHA256 bf615d1dcf2193b1c277599c2730ab3e1da01001b7e42927c77c5cbe044a74e6.
* C: notes/research_arbitrary_power_source_compilation.md,
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f.
* G: notes/actual_filling_fourier_hermite_gram.md,
  SHA256 9345e275c4c086b5f18ff2ded0f78e41e700a58b601bebd4b5e953f64e1b0d88.

K supplies the full splitting and polynomial crossing bounds.
C supplies the actual free-boundary compiler and Frobenius identity
kernel. G supplies the exact normalization packet (16), its two
filled values (19), and its all-width insertion into an exterior.
The comparison, residual bound and elementary exponential estimate
are proved above. Only written mathematics and text/hash operations
were used; frozen sources and public manuscripts are unchanged.
