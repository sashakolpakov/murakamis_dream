# A normalized Gaussian window for one original crossing

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The original crossing sends an explicit normalized coherent vector to a
nonzero Gaussian window, with its amplitude determined directly by the
finite matrix. This is an independent one-step norm-growth estimate.
The literal inverse, however, cannot be localized to the same two real
color windows. An example using the actual two-crossing column retains
its endpoint pin and an exponentially small relative equation residual,
but loses a macroscopic part of the source after inversion.

These statements concern the original Newton coefficient space. They
do not exclude an inverse on a larger complex analytic domain with
appropriate weights, or assert a packet for arbitrary short tangles.

## 1. Exact kernel and its regular bulk chart

Put \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(\eta=(-1)^D\), and \(\kappa=q^{D^2/2}\), with the displayed
logarithm of \(q\). The original crossing is
\[
 M_{jk}=\kappa(-1)^j q^{j(k+1)}
              \frac{S_j}{S_kS_{j-k}}\quad(0\le k\le j<N),
 \qquad S_j=\prod_{r=1}^j2\sin(\pi r/N).
 \tag{1}
\]
Outside this triangle its entries vanish exactly.
Its inverse is \(\overline M\). The reversal is exactly
\((Jf)_j=f_{D-j}\), with no approximation or change of norm.
These are the full physical-algebra matrices, including the normal
directions at double roots.

Write
\[
 \mathcal J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 E(x,y)=\mathcal J(x)-\mathcal J(y)-\mathcal J(x-y).
 \tag{2}
\]
Keeping \(\kappa\) exact, the regular bulk kernel is
\[
 M_{jk}=\frac{\kappa e^{i\pi x}}{\sqrt{2N}}
 \sqrt{\frac{\sin\pi x}{\sin\pi y\,\sin\pi(x-y)}}
 \exp N\{E(x,y)+i\pi x(y+1)\}
                 (1+O(N^{-1})),
 \quad x=j/N,\ y=k/N.
 \tag{3}
\]
The error is uniform on compact subsets of \(0<y<x<1\).
Its specified factorial interpolation has the corresponding
holomorphic expansion and fixed derivatives on a sufficiently small
complex neighborhood. This is the transpose convention of
[the existing kernel calculation](research_corner_newton_source_transport.md),
Section 3, with its level scalar left unexpanded. In particular
\((-1)^j=e^{i\pi j}\) is the chosen interpolation; it has not
been silently continued with the opposite logarithm.

For later global bounds, direct differentiation gives
\[
 E''=\pi
 \begin{pmatrix}
 \cot\pi x-\cot\pi(x-y)&\cot\pi(x-y)\\
 \cot\pi(x-y)&-\cot\pi y-\cot\pi(x-y)
 \end{pmatrix},\qquad \det E''=\pi^2.
 \tag{4}
\]
Its first diagonal is
\(-\pi\sin(\pi y)/[\sin(\pi x)\sin(\pi(x-y))]<0\);
thus it is negative definite throughout the strict triangle.
The entropy extends continuously to the closed triangle, is zero
on its boundary, and has its unique maximum at
\[
 (x_0,y_0)=(2/3,1/3),\qquad
 c=E(x_0,y_0)=-3\mathcal J(1/3)=2\mathcal J(5/6)>0.
 \tag{5}
\]
The last equality follows from reflection and duplication of
\(\mathcal J\). At this maximum, putting \(\beta=\pi/\sqrt3\),
\(E''=\beta\left(\begin{smallmatrix}-2&1\\1&-2\end{smallmatrix}\right)\).
The uniform estimate
\(\log S_j=N\mathcal J(j/N)+O(\log N)\) also holds at the
finite endpoints. It therefore gives a strict exponential kernel
gap outside every fixed neighborhood of (5).

## 2. A source-normalized one-step Gaussian estimate

Fix a real number \(a>0\). Define an exactly normalized vector by
\[
 f_{N,k}=Z_N^{-1}
       \exp\!\left[-\frac{a(k-N/3)^2}{2N}
                            -\frac{2\pi i k}{3}\right],
 \qquad
 Z_N^2=\sum_{k=0}^{D}e^{-a(k-N/3)^2/N}.
 \tag{6}
\]
Thus \(\|f_N\|_2=1\), including when \(3\) does not divide \(N\).
Gaussian summation gives
\(Z_N=N^{1/4}(\pi/a)^{1/4}(1+O(e^{-c_aN}))\) for some
\(c_a>0\). Set
\[
 \begin{split}
 A_a&=a+2\beta,&
 B_a&=2\beta-\frac{(\beta+i\pi)^2}{A_a},\\
 L_a&=(a/\pi)^{1/4}3^{-1/4}\sqrt{2\pi/A_a},&
 \nu_N&=\kappa e^{\,2\pi i/3-2\pi iN/9}.
 \end{split}
 \tag{7}
\]
Here \(L_a>0\) and
\(\Re B_a=2\beta+2\pi^2/(3A_a)>0\).

**Theorem 1.** On the entire original finite color interval,
define
\[
 g_{N,j}=\nu_N L_aN^{-1/4}e^{Nc}
       e^{4\pi i j/3}
       \exp\!\left[-\frac{B_a(j-2N/3)^2}{2N}\right].
 \tag{8}
\]
Then
\[
 \|Mf_N-g_N\|_2=O(N^{-1/2}e^{Nc}),\qquad
 \|Mf_N\|_2=e^{Nc}
       \left\{L_a(\pi/\Re B_a)^{1/4}+O(N^{-1/2})\right\}.
 \tag{9}
\]
In particular the leading coefficient is nonzero. This estimate
does not assume a nonzero input or output asymptotic coefficient:
the exact input and its normalization are (6).

*Proof.* Put \(X=(j-2N/3)/\sqrt N\) and
\(Y=(k-N/3)/\sqrt N\). The exponent of (3), multiplied by
the actual carrier in (6), has the expansion
\[
 Nc-\beta X^2+(\beta+i\pi)XY
       -\frac{A_aY^2}{2}
       +i(4\pi j/3-2\pi N/9).
 \tag{10}
\]
Its omitted cubic and higher terms are \(O(N^{-1/2})\)
times fixed polynomials in \(X,Y\) on bounded rescaled sets.
The leading density in (3) is \(3^{-1/4}N^{-1/2}\);
its remaining factor \(e^{i\pi x}\) has leading value
\(e^{2\pi i/3}\). The \(k\)-sum has mesh \(N^{-1/2}\), and
\[
 \int_{\mathbb R}e^{-A_aY^2/2+(\beta+i\pi)XY}\,dY
       =\sqrt{2\pi/A_a}\,
              e^{(\beta+i\pi)^2X^2/(2A_a)}.
 \tag{11}
\]
This proves (8) locally with the displayed scalar and density.

For error control, choose a fixed small neighborhood of (5).
The real Hessian there is uniformly negative definite, so the
absolute summand is bounded by a fixed polynomial times
\(e^{Nc-c_1(X^2+Y^2)}\). Taylor's formula and a smaller
neighborhood absorb its cubic remainder into this Gaussian;
the integrated error is \(O(N^{-1/2})\) times polynomial
Gaussian moments. Gaussian sum-to-integral errors obey the
same bound uniformly in the fractional centers. Outside the
neighborhood, (4)--(5) and the endpoint-uniform factorial bound
give a polynomial times \(e^{N(c-\delta)}\), with \(\delta>0\).
These estimates prove the stated global \(\ell^2\) error.
Finally sum \(|g_{N,j}|^2\), again with mesh \(N^{-1/2}\),
and use \(\Re B_a>0\) to obtain (9). \(\square\)

Conjugating the input and output gives the corresponding theorem
for \(M^{-1}=\overline M\); its forward triangle is still \(k\le j\).
This conjugate theorem is not an inverse between the two windows
in (6) and (8). Nor does Theorem 1 identify (6) with the boundary
state of an arbitrary fixed tangle.

## 3. Why the actual inverse needs more than the dominant window

Let \(P_I,P_J\) be coordinate projections onto two disjoint color
intervals with \(\max I<\min J\). Lower triangularity gives
\[
                  P_I M^{-1}P_J=0
 \tag{12}
\]
exactly. Thus the dominant map from a window near \(N/3\) to one
near \(2N/3\) in Theorem 1 has no literal inverse obtained by
restricting \(M^{-1}\) to those two real windows.

This is compatible with the exact finite inverse identity.
In the \(Q\)-binomial form
\(M_{jk}=\kappa(-q)^j q^{k^2}{j\brack k}_Q\), its
\((j,\ell)\) product entry, with \(d=j-\ell\ge0\), is
\[
 (M^{-1}M)_{j\ell}
 =(-1)^d q^{-d(2\ell+1)}{j\brack\ell}_Q
                          (Q^{1-d};Q)_d.
 \tag{13}
\]
For \(d>0\), the final finite product contains \(1-Q^0=0\);
for \(d=0\) the expression is one. This follows by multiplying
the two triangular kernels and applying the finite \(Q\)-binomial
theorem. All indices stay below \(N\), so no denominator vanishes.
The cancellation in (13) is part of the inverse, not an omitted
endpoint error.

There is a particularly explicit original-source example. Put
\(\alpha_1=M\mathbf e_0\), \(\alpha_2=M^2\mathbf e_0\). Finite
binomial summation gives
\[
 (\alpha_1)_j=\kappa(-q)^j,\qquad
 (\alpha_2)_j=\kappa^2 i^j q^{j(j+3)/2}S_j.
 \tag{14}
\]
One can also obtain this from the exact coherent-feature identity
in [the frame transport note](research_gaussian_frame_newton_transport.md).
In particular \(\|\alpha_1\|=\sqrt N\), whereas \(\alpha_2\)
has its unique factorial concentration at \(j/N=5/6\).

Fix \(0<\delta<1/12\), let \(P_B\) retain
\(|j/N-5/6|<\delta\), and preserve the exact source pin by defining
\[
                  \widetilde\alpha_2
                   =P_B\alpha_2+\kappa^2\mathbf e_0 .
 \tag{15}
\]
The factorial entropy has its unique maximum at \(5/6\), so
\[
 \frac{\|\widetilde\alpha_2-\alpha_2\|_2}{\|\alpha_2\|_2}
                         \le C N^C e^{-\epsilon_\delta N}
 \tag{16}
\]
for some \(\epsilon_\delta>0\). The first coordinate in (15)
is exact. More strongly, the original lower bidiagonal coordinate
\[
 K_{jj}=-q^{-1}Q^{-j},\qquad K_{j,j-1}=1-Q^{-j}
 \tag{17}
\]
satisfies \(K\alpha_2=\eta\mathbf e_0\) and \(\|K\|_2\le3\).
Hence (15) keeps its forced first row exactly and has an
exponentially small relative equation residual in the norm of
\(\alpha_2\), by (16).

Nevertheless, for every \(j/N<5/6-\delta\), (12) and (14) give
\[
 (M^{-1}\widetilde\alpha_2-\alpha_1)_j
   =\kappa(-1)^j(q^{-j}-q^j)
   =-2i\kappa(-1)^j\sin(\pi j/N).
 \tag{18}
\]
Writing \(b=5/6-\delta\), it follows that
\[
 \liminf_{N\to\infty}
 \frac{\|M^{-1}\widetilde\alpha_2-\alpha_1\|_2^2}
      {\|\alpha_1\|_2^2}
       \ge 4\int_0^b\sin^2(\pi x)\,dx
       =2b-\frac{\sin(2\pi b)}{\pi}>0.
 \tag{19}
\]
Thus an exponentially accurate relative approximation, even with
the actual pin and a small relative equation residual, need not
survive the next short crossing. The example uses literal
original columns and \(M^{-1}M^2=M\); it does not assert a failure
of a reduced hyperbolic tangle theorem.

The factorially weighted Green estimates in
[the exact weighted transport theorem](research_elementary_weighted_green_transport.md)
do retain these tails. A general composition result would have to
transport those weights, or an equivalent complete analytic state,
through every crossing and reversal. Theorem 1 supplies a true
nonzero one-step Gaussian coefficient; (12)--(19) explain why
its dominant real-color window alone does not supply an inverse
or a general short-word lower bound.

## 4. The normalized operator limit

The Gaussian estimate also holds at the operator level. Let
\(I_{{\rm in},N}\) embed \(\ell^2(\{0,\ldots,D\})\) isometrically
in \(L^2(\mathbb R)\) by giving a vector entry \(v_k\) the constant
value \(N^{1/4}v_k\) on the interval of length \(N^{-1/2}\)
centered at \(Y_k=(k-N/3)/\sqrt N\), and zero elsewhere.
Define \(I_{{\rm out},N}\) in the same way with centers
\(X_j=(j-2N/3)/\sqrt N\). Set
\[
 \widetilde M_{jk}
   =\nu_N^{-1}e^{-Nc}e^{-4\pi i j/3}
                              M_{jk}e^{-2\pi i k/3},\qquad
 \mathcal T_N=I_{{\rm out},N}\widetilde M I_{{\rm in},N}^*.
 \tag{20}
\]
All gauges except \(e^{-Nc}\) have modulus one.

**Theorem 2.** The operators \(\mathcal T_N\) converge in
Hilbert--Schmidt norm, with error \(O(N^{-1/2})\), to the integral
operator with kernel
\[
 \mathcal K(X,Y)=3^{-1/4}
       e^{-\beta(X^2+Y^2)+(\beta+i\pi)XY}.
 \tag{21}
\]
Consequently
\[
 \begin{split}
 \|M\|_{\rm HS}
    &=e^{Nc}\{3^{-1/4}+O(N^{-1/2})\},\\
 \|M\|_2
    &=e^{Nc}\{\|\mathcal K\|_{2\to2}+O(N^{-1/2})\}.
 \end{split}
 \tag{22}
\]
The same bounds hold for \(M^{-1}\).

*Proof.* On the two cells indexed by \(j,k\), the kernel of
\(\mathcal T_N\) is \(\sqrt N\,\widetilde M_{jk}\).
Expansion (3) and the exact carrier calculation (10) give (21).
More quantitatively, set \(h=N^{-1/2}\). On a fixed sufficiently
small physical neighborhood of (5), Taylor's formula, the uniform
density estimate and negative real Hessian give
\[
 |\sqrt N\,\widetilde M_{jk}-\mathcal K(X_j,Y_k)|
 \le Ch(1+|X_j|+|Y_k|)^m e^{-c_1(X_j^2+Y_k^2)}
\]
for fixed \(C,m,c_1>0\). The cubic remainder is bounded by
\(Ch(|X_j|+|Y_k|)^3\); shrinking the physical neighborhood
absorbs its exponential into the quadratic Gaussian. Each cell
has area \(h^2\), and
\(h^2\sum_{j,k}(1+|X_j|+|Y_k|)^{2m}
e^{-2c_1(X_j^2+Y_k^2)}\) is uniformly bounded. The squared
error on these cells is therefore \(O(h^2)\).
Outside the physical neighborhood, (5) and the uniform endpoint
factorial estimate give a polynomial times \(e^{-\delta N}\)
in the normalized matrix norm.

On each cell, the mean-value formula for the explicit Gaussian
gives
\[
 |\mathcal K(X,Y)-\mathcal K(X_j,Y_k)|
 \le Ch(1+|X|+|Y|)e^{-c_2(X^2+Y^2)}.
\]
This gives \(O(h)\) error in \(L^2(dX\,dY)\). The omitted cells
and the finite triangular boundary have rescaled distance of
order \(\sqrt N\) from the origin and contribute only Gaussian
tails. These estimates prove Hilbert--Schmidt convergence.
Finally,
\[
 \|\mathcal K\|_{\rm HS}^2
   =3^{-1/2}\int_{\mathbb R^2}
       e^{-2\beta(X^2+Y^2)+2\beta XY}\,dX\,dY
   =\frac1{\sqrt3}.
 \tag{23}
\]
Operator-norm convergence follows from Hilbert--Schmidt
convergence, and \(\mathcal K\ne0\). Since \(M^{-1}=\bar M\),
both matrix norms agree with those of the inverse. \(\square\)

This is a compact Gaussian integral operator, not a boundedly
invertible operator on \(L^2(\mathbb R)\). The finite matrices
remain invertible: indeed
\(\|\widetilde M^{-1}\|_2
=e^{Nc}\|M^{-1}\|_2
=e^{2Nc}(\|\mathcal K\|_{2\to2}+O(N^{-1/2}))\).
The original endpoint vector is sent by the input embedding
to a cell centered at \(-\sqrt N/3\), outside the limiting
Gaussian window. Thus (20)--(23) do not silently turn the
original cap into a specified interior Gaussian.

The bound \(\|M^{\pm1}\|_2\le C e^{Nc}\) can propagate
errors without an extra polynomial loss when a subsequent
step has a separately established gain of that same rate.
For a general original word, establishing that gain and the
correct boundary observation remains necessary. The exact
relative-error failure (15)--(19) persists; neither the
operator limit nor its positive Gaussian real part supplies
the missing global inverse or the original cap contribution.

## 5. The actual singular gap and the original cap

The limiting operator has an explicit singular spectrum. Put
\[
 \rho=\frac{2}{5+\sqrt{21}}=\frac{5-\sqrt{21}}2,\qquad
 \gamma=\frac{\sqrt{21}}2\,\beta .
 \tag{24}
\]
Direct Gaussian integration gives the kernel
\[
 (\mathcal K^*\mathcal K)(Y,Z)
 =\frac1{\sqrt2\,3^{1/4}}
 e^{-(5\beta/4)(Y^2+Z^2)+\beta YZ+i\pi(Z^2-Y^2)/4}.
 \tag{25}
\]
Conjugation by multiplication by \(e^{-i\pi Y^2/4}\)
removes its imaginary quadratic part. Its remaining real
Gaussian kernel has eigenvalues
\(\sqrt\rho\,\rho^m\), \(m=0,1,\ldots\), on the normalized
Hermite functions of width \(\gamma\).
This is the classical Mehler calculation; see
[NIST DLMF, equation 18.18.28](https://dlmf.nist.gov/18.18.E28).
The direct verification below fixes its constants for this
original crossing rather than assuming a source normalization.

Here is a direct verification of the normalization and ratio.
Write \(d=(5+\sqrt{21})\beta/4\) and
\(C=1/(\sqrt2\,3^{1/4})\). Integrate the Hermite generating
function
\(e^{-\gamma Z^2/2}e^{2\sqrt\gamma Zt-t^2}\)
against the real kernel in (25). The result is
\[
 C\sqrt{\pi/d}\ e^{-\gamma Y^2/2}
      e^{\,2\sqrt\gamma Y\rho t-\rho^2t^2}.
 \tag{26}
\]
Indeed \(\beta/(2d)=\rho\),
\(\gamma/d-1=-\rho^2\), and
\(C\sqrt{\pi/d}=\sqrt\rho\).
Coefficient comparison and completeness of the Hermite basis
give the stated spectrum. Thus
\(\|\mathcal K\|=\rho^{1/4}\), and the squared singular
gap is \(\sqrt\rho(1-\rho)>0\).

**Corollary 3.** Let \(s_0(N)\ge s_1(N)\) be the two largest
singular values of the actual crossing. Then
\[
 s_0(N)=e^{Nc}\{\rho^{1/4}+O(N^{-1/2})\},\qquad
 s_1(N)=e^{Nc}\{\rho^{3/4}+O(N^{-1/2})\}.
 \tag{27}
\]
For sufficiently large \(N\) its top right singular vector
\(v_N\) is unique up to phase. The actual original cap obeys
\[
 \begin{split}
 |\langle v_N,\mathbf e_0\rangle|^2
       &\le \frac{N}{s_0(N)^2}=O(Ne^{-2Nc}),\\
 \left\langle\mathbf e_0,
  \left(I-\frac{M^*M}{s_0(N)^2}\right)\mathbf e_0\right\rangle
       &=1-\frac{N}{s_0(N)^2}\longrightarrow1.
 \end{split}
 \tag{28}
\]
The positive operator \(M^*M/s_0(N)^2\) has top eigenvalue
one and gap \(1-\rho+O(N^{-1/2})\). Thus this gap is an
actual proved property of the finite crossing, but its original
cap is not almost invariant for that operator.

*Proof.* Hilbert--Schmidt convergence in Theorem 2 implies
operator-norm convergence and convergence of the ordered
singular values, with the same error. Apply (25)--(26).
Finally \(M\mathbf e_0=\kappa((-q)^j)_j\), so its norm
squared is exactly \(N\). Its expansion in right singular
vectors has contribution
\(s_0(N)^2|\langle v_N,\mathbf e_0\rangle|^2\), which
proves both formulas in (28). \(\square\)

This is a statement about the unweighted original cap and this
particular positive operator. It does not exclude a weighted or
complex-transported state with a useful observation bound.
It shows explicitly why the existence of a well-separated
Gaussian singular mode does not supply the cap's geometric
coefficient.

## 6. Reproduction

The [focused checker](../experiments/check_one_crossing_gaussian_window.py)
builds small-level crossing matrices independently by polynomial
multiplication in the full Newton quotient. It checks the exact
columns, conjugate inverse, endpoint forcing, retained pin and
lower-color inverse discrepancy, together with the Mehler constants.
The [saved result](../repro/results/research-one-crossing-gaussian-window.json)
records 998 finite identities at 100 decimal digits, with maximum
relative error below \(9.42\cdot10^{-98}\), and both level parities.
It also records six larger-level Gaussian and singular-value
comparisons as diagnostics only. They are not used to prove the
operator limit or the uniform error estimates. The script and its
direct project dependency have recorded hashes.
