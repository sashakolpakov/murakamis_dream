# Finite-branch reciprocity retaining the original twist normals

Private written proof, 14 November 2026. For every fixed nonzero
integer twist power \(p\), the complete Fourier--Hermite kernel of
\(R^{2p}\) has an exact representation by \(2|p|\) real Fresnel
branches. Their scalar phases are explicit units. The first-normal
data become a bounded periodic sawtooth amplitude; they are not
discarded or reconstructed from a value-only Gauss sum.

This compresses the infinite charge representation already in
[the coherent Gaussian note](actual_coherent_filling_gaussian_chirp.md).
It is an exact identity on the original integer color grid, with
ordinary Cauchy principal values. It neither supplies a holomorphic
complex-color continuation of these sawtooth integrals nor proves
that a branch survives an exterior contraction.

## 1. Original data and the finite-branch formula

Use the conventions and full Hermite data of
[the original twist kernel](actual_twist_circle_fourier_kernel.md):

\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad\kappa=q^{d^2/2},\quad t_k=(k+\tfrac12)/N.
\]

All fractional powers use this displayed logarithm. For \(p\in
\mathbb Z\setminus\{0\}\), put

\[
 h_k=Q^{pk(k+1)},\qquad
 d_k=-p(d-2k)h_k=2pN(t_k-\tfrac12)h_k,
\]
\[
 H_n=\frac1N\sum_{k=0}^{N-1}h_k e^{-2\pi i n t_k},\qquad
 D_n=\frac1N\sum_{k=0}^{N-1}d_k e^{-2\pi i n t_k}.
 \tag{1}
\]

The canonical Chebyshev coefficients are

\[
 a_n=\frac{D_n+(N-n)H_n}{N},\quad 0\le n<N.
 \tag{2}
\]

Here \(D_0=0\), so \(a_0=H_0\). Formula (2) includes the actual
paired-node derivatives and the odd simple node.

For a real argument define the periodic sawtooth

\[
 s(u)=\frac12-\{u\}\quad(u\notin\mathbb Z),\qquad s(u)=0
 \quad(u\in\mathbb Z).
 \tag{3}
\]

Its values at integers affect no integral. For an integer \(n\), and
\(r=0,\ldots,2|p|-1\), define

\[
 b_r=n+Nr,\quad B_r=\frac12-\frac{b_r}{2pN},\qquad
 C_r=(-1)^r\exp\left(-\pi i b_r-\frac{\pi i b_r^2}{2pN}\right),
 \tag{4}
\]
\[
 G_{p,N}=\frac{e^{i\operatorname{sgn}(p)\pi/4}}
                    {\sqrt{2|p|N}},\qquad
 J_r=\operatorname{PV}\int_{\mathbb R}
            s(B_r-v)e^{2\pi i pN v^2}\,dv.
 \tag{5}
\]

The principal value in (5) is the limit over \([-L,L]\). It exists;
the proof below retains the inherited endpoint prescription.

**Theorem.** For every \(N\ge2\), every nonzero integer \(p\), and
every integer \(n\), the transforms (1) satisfy

\[
 \boxed{H_n=\kappa^{-p}G_{p,N}\sum_{r=0}^{2|p|-1}C_r,\qquad
 D_n=2pN\kappa^{-p}\sum_{r=0}^{2|p|-1}C_r J_r.}
 \tag{6}
\]

Consequently, for the physical coefficient range \(0\le n<N\),

\[
 \boxed{a_n=\kappa^{-p}\sum_{r=0}^{2|p|-1}C_r
   \operatorname{PV}\int_{\mathbb R}
   [1-n/N+2p\,s(B_r-v)]e^{2\pi i pN v^2}\,dv.}
 \tag{7}
\]

Every \(C_r\) has modulus one and \(G_{p,N}\ne0\). There is no
division by a Gauss sum or a coprimality hypothesis. The finite sum
in the first formula of (6) retains all gcd and parity zeros. The
normal formula remains present even at a color where that finite
sum vanishes. Neither \(J_r\) nor a complete branch integral is
asserted nonzero.

## 2. Proof with the original normal weight

The centered Gaussian identity proved from the full original
spectral data is

\[
 h_k=\kappa^{-p}
         e^{2\pi i pN(t_k-1/2)^2}.
 \tag{8}
\]

For \(b\in\mathbb Z\) set

\[
 I(b)=\int_0^1e^{2\pi i pN(t-1/2)^2-2\pi i bt}\,dt,
\]
\[
 K(b)=\int_0^1 2pN(t-\tfrac12)
                   e^{2\pi i pN(t-1/2)^2-2\pi i bt}\,dt.
 \tag{9}
\]

Midpoint Fourier sampling of the smooth interval functions gives

\[
 H_n=\kappa^{-p}\sum_{\ell\in\mathbb Z}^{\rm sym}
                     (-1)^\ell I(n+N\ell),\qquad
 D_n=\kappa^{-p}\sum_{\ell\in\mathbb Z}^{\rm sym}
                     (-1)^\ell K(n+N\ell).
 \tag{10}
\]

For completeness, periodically extend each interval function and
take its symmetric Fourier series. Its values at the interior
midpoints converge to the original values. Averaging those \(N\)
values kills all Fourier modes except the multiples of \(N\),
which have midpoint multiplier \((-1)^\ell\). This proves (10)
with its specified summation. No equality of endpoint derivatives
is used for the normal integrand.

The endpoint values of the unweighted Gaussian factor at \(t=0,1\)
are equal. Integration by parts in the ordinary Fourier transform
therefore gives \(I(n+N\ell)=O(\ell^{-2})\). For the normal
integrand its endpoint difference is

\[
 2pN e^{\pi i pN/2},
\]

and two integrations by parts give

\[
 K(n+N\ell)=
 -\frac{2pN e^{\pi i pN/2}}{2\pi i(n+N\ell)}
                         +O(\ell^{-2}).
 \tag{11}
\]

These statements concern the tails; any zero denominator is a
finite middle term and is evaluated by (9). Constants may depend
on \(N,p,n\). In particular each fixed residue class modulo
\(2|p|\), summed symmetrically in its class parameter, converges.
Replacing a common symmetric cutoff by the union of finitely many
such class cutoffs changes only a bounded number of tail terms,
each tending to zero. Hence (10) may be regrouped in these classes.

Write

\[
 \ell=r+2pm,\qquad m\in\mathbb Z,
 \quad r=0,\ldots,2|p|-1.
\]

This also covers negative \(p\). Complete the square in (9) by

\[
 v=t-\frac12-\frac{n+N\ell}{2pN}.
\]

The interval becomes \([B_r-1-m,B_r-m]\). Its scalar phase is

\[
 (-1)^\ell e^{-\pi i(n+N\ell)
                         -\pi i(n+N\ell)^2/(2pN)}=C_r.
 \tag{12}
\]

Indeed increasing \(\ell\) by \(2p\) changes that expression by
\(e^{-2\pi i(n+N\ell)-4\pi i pN}=1\). This is the exact step
where the integer color is used. In particular it retains every
parity phase rather than normalizing a nonzero Gauss sum.

The intervals \([B_r-1-m,B_r-m]\) tile the real line. On their
interiors \(m=\lfloor B_r-v\rfloor\), and the original normal
weight becomes

\[
 \begin{split}
 2pN(t-\tfrac12)
 &=2pNv+n+Nr+2pNm\\
 &=2pN\left(\frac12-\{B_r-v\}\right)
 =2pN s(B_r-v).
 \end{split}
 \tag{13}
\]

Thus the sawtooth is the literal unwrapped linear normal weight
after reciprocity. It is not an added regulator or an error term.
Keeping \(m=-M,\ldots,M\) gives the ordinary integrals over

\[
 [B_r-1-M,B_r+M].
 \tag{14}
\]

Their limits exist by the grouped convergence just proved. The
center of (14) is the fixed number \(B_r-1/2\). They have the same
limit as symmetric intervals about zero: the difference consists
of two intervals of bounded length at distance tending to infinity.
The sawtooth is bounded and has bounded variation on each such
interval, uniformly in its location. Splitting at its finitely
many jumps and integrating \(e^{2\pi i pNv^2}\) by parts therefore
bounds these differences by \(O(M^{-1})\). The same argument
applies to a bounded partial final unit interval, so this is the
full Cauchy principal-value limit, not only an integer subsequence.

The unweighted tiled integral is the ordinary Fresnel integral
\(G_{p,N}\). One may evaluate it by first integrating
\(e^{-(\varepsilon-2\pi i pN)v^2}\) for \(\varepsilon>0\) and then
letting \(\varepsilon\downarrow0\); integration by parts on both
tails identifies that limit with the ordinary Fresnel improper
integral. Equations (12)--(14) now prove (6), and (2) proves (7).

## 3. Full operator and prescribed closing

Let \(E_0(z)=1\), \(E_n(z)=2T_n(z/2)\) for \(n\ge1\). For each
branch define the polynomial of degree less than \(N\), with piecewise
smooth real parameter \(v\),

\[
 \mathcal B_r(v;z)=\sum_{n=0}^{N-1}C_r(n)
 [1-n/N+2p\,s(B_r(n)-v)]E_n(z).
 \tag{15}
\]

The dependencies \(C_r(n),B_r(n)\) are those of (4). Because
\(f_{N,2p}(z)=\sum_n a_nE_n(z)\), (7) gives the exact polynomial
identity

\[
 f_{N,2p}(z)=\kappa^{-p}\sum_{r=0}^{2|p|-1}
   \operatorname{PV}\int_{\mathbb R}
          e^{2\pi i pNv^2}\mathcal B_r(v;z)\,dv.
 \tag{16}
\]

The integral is coefficientwise in a finite-dimensional polynomial
space. Evaluating on the original pair Casimir therefore gives

\[
 \boxed{R^{2p}=\kappa^p\sum_{r=0}^{2|p|-1}
   \operatorname{PV}\int_{\mathbb R}
       e^{2\pi i pNv^2}\mathcal B_r(v;\Omega)\,dv.}
 \tag{17}
\]

This is full Hermite functional calculus: the \(D_n\) that determine
all repeated-node derivatives were used in (2) and (13). The odd
simple node and the even middle Fourier alias retain their original
conditions through the original interpolation theorem.

Every fixed exterior contraction, original pivotal cut, or actual
linear quarter-turn commutes with (17), by finite-dimensional
linearity. For example, for any such exterior functional \(\Lambda\),

\[
 \Lambda(R^{2p})=\kappa^p\sum_r\operatorname{PV}
       \int_{\mathbb R}e^{2\pi i pNv^2}
                      \Lambda(\mathcal B_r(v;\Omega))\,dv.
 \tag{18}
\]

No new closing vector is chosen. Several fixed disjoint twist slots
may be replaced using iterated principal values, or coefficientwise
rectangular limits; the scalar factors in the finite tensor sum
then converge separately. No unsupported absolute Fubini interchange
is needed. Neighboring Casimir operators are not commuted.

In the ordinary circle basis the original endpoint convention is
still

\[
 \beta_j=(-1)^j(a_j-a_{j+2}),\qquad a_N=a_{N+1}=0.
\]

Values of the integer interpolation (7) outside its canonical range
must not replace these two zero endpoint coefficients.
For \(p=0\), use the separate exact identity \(R^0=I\),
\(H_n=\delta_{n0}\), \(D_n=0\) on \(0\le n<N\).

## 4. Gain and limits

The value reciprocity in (6) is the usual finite quadratic Gauss
compression. Its full-normal companion, the second formula of (6),
retains the finite-window jump as a bounded sawtooth. Thus the
infinite charge representation can be replaced exactly by \(2|p|\)
real integral branches for the entire original twist operator.
The number is independent of \(N\); the polynomial degree and the
remaining physical color space still grow with \(N\).

For a fixed \(N\), no approximation, limit interchange in \(N\), or
discarded normal term enters the identity. For a fixed \(p\), each
branch amplitude in (7) is bounded on the real line by
\(1+|p|\) in the physical range. This is a pointwise amplitude bound,
not a lower bound for its oscillatory integral or exterior pairing.

The sawtooth jumps are essential. If \(n\) is allowed to be complex,
the ratio in (12) becomes \(e^{-2\pi i n}\), and the tiled branch
acquires an additional factor \(e^{-2\pi i nm}\). Thus (6)--(7)
must not be analytically continued by keeping the same bounded
sawtooth formula. The entire finite interpolation and its endpoint
current are already supplied by the coherent Gaussian note. A
complex deformation must use that whole formula or prove an
appropriate new convergence and endpoint prescription.

The present result therefore gives an exact fused source expression,
not positive local shapes, a deformation to a geometric saddle, a
nonzero original contour intersection, or the volume identity.

## Direct source versions

Both sources were read as written mathematics; no mathematical code,
test, numerical evaluation, import, or compilation was used.

- `actual_twist_circle_fourier_kernel.md`:
  `1d93f6f13d271c56eee6e7ea8ddf5b9ea0eea92a2076ede7068df552bab94292`.
- `actual_coherent_filling_gaussian_chirp.md`:
  `d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522`.
