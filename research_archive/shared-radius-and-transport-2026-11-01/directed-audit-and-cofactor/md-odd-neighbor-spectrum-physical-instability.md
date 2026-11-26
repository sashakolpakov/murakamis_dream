# Physical-side instability of the complete odd central source

This note concerns the original cleared central source, before any shared-face coefficient extraction. It gives an obstruction to extending the endpoint **real-stability argument itself** to a one-sided physical spectral neighborhood. It gives no obstruction to a signed stable decomposition, to a coherent norm estimate, or to the desired full-source exponential bound.

## 1. Original finite source and statement

Let \(N=2m+1\), \(\theta=\pi/N\), and put

\[
s_j=2\sin(j\theta),\qquad
 a_r=4\cos^2((r+\tfrac12)\theta),\qquad
 u=-2-\sigma.
\tag{1}
\]

The physical neighboring interval \(\sigma\in[-2,-2+\varepsilon]\) is therefore \(u\in[-\varepsilon,0]\). With \(R_0=1\), \(R_{-1}=0\), the original cofactors satisfy

\[
R_j(b;x,y;u)
=b^j\prod_{r=0}^{j-1}(a_r+u)
+s_j^2(x+y)R_{j-1}(b;x,y;u)
+s_js_{j-1}(a_{j-1}+u)xyR_{j-2}(b;x,y;u).
\tag{2}
\]

Set \(G_b(u)=R_m(b;x,y;u)\) and \(D_b(u)=R_{m-1}(b;x,y;u)\). The actual odd central polynomial is

\[
\mathcal P_N(x,b,c,y;u)
=G_b(u)G_c(u)+u s_m^2xyD_b(u)D_c(u).
\tag{3}
\]

There is no replacement of (3) by its visited product, and its skipping coefficient has its original sign. Every term has the original face degree \(2m=N-1\). The exact source normalization of (2)–(3) is the one in `actual_cross_cofactor_factorization.md`, Sections 1–2; no row, factorial, or scalar has been removed.

A real polynomial is called *real stable* if it has no zero when all of its variables have strictly positive imaginary parts.

**Theorem.** There is an odd-level threshold \(N_0\) such that, for every odd \(N\ge N_0\), there exists \(\varepsilon_N>0\) with the following property:

\[
\begin{gathered}
0<\varepsilon<\varepsilon_N
\quad\Longrightarrow\quad
\mathcal{P}_N(x,b,c,y;-\varepsilon)\text{ is not real stable.}
\end{gathered}
\tag{4}
\]

In particular no fixed one-sided physical spectral neighborhood of \(-2\) can consist of real-stable central source polynomials at all large odd levels. The threshold \(\varepsilon_N\) in this proof is not uniform in \(N\); (4) still suffices for the stated obstruction.

## 2. Endpoint determinant and simple roots

At \(u=0\), the exact determinant identification is

\[
G_b(0)=N\det\left(bI+\frac{xH_-+yH_+}{2}\right),
\tag{5}
\]

where the actual \(m\)-by-\(m\) positive Hermitian matrices have diagonal

\[
(H_\pm)_{j,j}=\frac1{\cos(j\theta)\cos((j+1)\theta)},
\quad 0\le j<m,
\tag{6}
\]

and upper adjacent entries

\[
(H_\pm)_{j-1,j}
=\sqrt{\beta_j}\bigl(\sin(j\theta)\pm i\cos(j\theta)\bigr),
\quad
\beta_j=\frac{\sin^2(j\theta)}
{\cos^2(j\theta)\sin((2j-1)\theta)\sin((2j+1)\theta)}.
\tag{7}
\]

Consequently \(J=(H_-+H_+)/2\) is a positive real symmetric tridiagonal matrix with every adjacent entry \(\sqrt{\beta_j}\sin(j\theta)>0\). Its eigenvalues are simple: the first coordinate of an eigenvector determines all remaining coordinates by the three-term equations, and a zero first coordinate would force the whole vector to vanish. Symmetry then excludes eigenvalue multiplicity.

Thus, with \(x=y=1\),

\[
G(b):=G_b(0)=N\prod_{i=1}^m(b-r_i),
\qquad r_1<\cdots<r_m<0.
\tag{8}
\]

Let \(D(b)=D_b(0)\) in the same specialization. Its degree is \(m-1\), and its leading coefficient is \(\prod_{r=0}^{m-2}a_r>0\). The independent hard-edge theorem `md-odd-lower-cofactor-hard-edge-obstruction.md` proves that \(D\) has nonreal roots at every sufficiently large odd level. More strongly, their number is unbounded with the level. Only existence of one nonreal root is used here.

## 3. An elementary residue obstruction

Define the real numbers

\[
h_i=\frac{D(r_i)}{G'(r_i)}.
\tag{9}
\]

Partial fractions give

\[
\frac{D(z)}{G(z)}=\sum_{i=1}^m\frac{h_i}{z-r_i},
\qquad
\sum_i h_i=\frac{\prod_{r=0}^{m-2}a_r}{N}>0.
\tag{10}
\]

If all \(h_i\) were nonnegative, then for every \(\operatorname{Im}z>0\),

\[
\operatorname{Im}\frac{D(z)}{G(z)}
=-\operatorname{Im}z\sum_i\frac{h_i}{|z-r_i|^2}<0.
\tag{11}
\]

This precludes every nonreal zero of \(D\): upper-half-plane zeros are impossible by (11), lower-half-plane zeros are their conjugates, and every zero common to \(D\) and \(G\) is real. Thus nonreal roots of \(D\) force a negative residue. The positive sum in (10) also forces a positive residue. We may therefore choose distinct indices \(i,j\) with

\[
h_i h_j<0.
\tag{12}
\]

This step retains the actual normalization: it does not suppose that the skipping cofactor is a principal minor of the visited determinant.

## 4. A zero inside the physical one-sided perturbation

Write \(\varepsilon=\eta^2\), with \(\eta>0\), and fix the indices from (12). In the actual source (3) set

\[
u=-\eta^2,\qquad x=y=1,\qquad
b=r_i+\eta z,\quad c=r_j+\eta z.
\tag{13}
\]

Since both visited factors vanish at \(\eta=0\), the quotient

\[
F(\eta,z)=\eta^{-2}
\mathcal P_N(1,r_i+\eta z,r_j+\eta z,1;-\eta^2)
\tag{14}
\]

has a removable singularity at \(\eta=0\) and is holomorphic there. Indeed the coefficients in (2) are polynomial in \(u\), and Taylor expansion gives

\[
F(0,z)=G'(r_i)G'(r_j)z^2-s_m^2D(r_i)D(r_j)
=G'(r_i)G'(r_j)\bigl(z^2-s_m^2h_i h_j\bigr).
\tag{15}
\]

The upper root

\[
z_0=i s_m\sqrt{-h_i h_j}
\tag{16}
\]

is nonzero and simple. The holomorphic implicit function theorem supplies a root \(z(\eta)\) of (14), with \(z(0)=z_0\), for all sufficiently small \(\eta\). For positive real \(\eta\), its imaginary part remains positive. Hence the specialized polynomial at \(x=y=1\) has a zero with both \(\operatorname{Im}b>0\) and \(\operatorname{Im}c>0\).

For completeness, this boundary specialization also yields a zero with *all four* imaginary parts positive. At the constructed zero,

\[
\partial_c\mathcal P_N
=\eta\,G'(r_i)G'(r_j)z(\eta)+O(\eta^2)\ne0
\tag{17}
\]

for sufficiently small positive \(\eta\). Keep \(b\) fixed and perturb \(x,y\) from \(1,1\) to \(1+i\delta,1+i\delta\). A second local implicit-function argument adjusts \(c\) continuously to maintain the zero. Choosing \(\delta>0\) sufficiently small preserves its strictly positive imaginary part. The spectral parameter remains the real physical value \(u=-\eta^2\). This proves (4).

## 5. Scope and the remaining analytic problem

The obstruction concerns a local, unextracted polynomial. It is enough to rule out a proof that every actual neighboring central coupon is itself real stable on a fixed physical interval, followed by products and coefficient extraction. It also rules out identifying \(D\) with a positive rank-one compression of the same endpoint pencil: such a compression would have nonnegative residues in (10).

It does not prove that the globally extracted exterior is unstable, because common face extraction can remove a local obstruction. It does not compare source growth rates, does not show a positive proportion of defective roots, and does not yield an exponential lower bound. In particular it leaves open a signed stable decomposition with controlled total cost, a non-diagonal coherent norm, and a source-exact evolution estimate preserving the cap cancellation. The original source phases and target loads are unchanged throughout.

The existing spectral nodal interpolation provides exact signed lower-channel expressions, but distant nodal weights are not exponentially small merely because the target spectrum is close to \(-2\). Therefore that identity, by itself, still does not transfer the endpoint cap gap. A successful decomposition must also control the response of its pieces after the *same* shared-face extraction, or retain the relevant interference before estimating them.


## 6. Existing two-port cancellation is compatible with this obstruction

The published `research_cap_cross_two_spectrum_neighborhood_stability.md` already proves a shrinking rate cost for a specific coherent contraction on complex disks around both spectral endpoints. Its exact incidence is \(E=(A,0,C,Z)\), \(F=(0,A,0,C)\), with \(A\) incident only to these two ports and extracted at its original target \(A^{N-1}\). Both local projectors, all remaining demands \(0\le n\le N-2\), and the extra odd central transition are retained. Its proof uses polynomial contiguity and both endpoint currents, rather than real stability of every raw coupon.

That theorem is not a fixed-neighbor theorem for an arbitrary protected singleton star: the boundary face may have further incidences, and its neighboring central coupon may retain two nonprotected outer faces. The R54 original exterior has precisely these broader features. The present local nonstability theorem neither contradicts nor extends the existing two-port cancellation estimate.
