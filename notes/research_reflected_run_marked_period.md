# A positive marked period for reflected crossing runs

Research note, 3 November 2026.

For two original even runs with opposite powers, a unit-modulus
Floquet mode gives a strictly positive marked period. The original
channel equations give a lower bound uniform in the quantum level.
Consequently the affine source row has a nonremovable pole at the
corresponding auxiliary clock, even when the classical determinant
root is multiple. This statement retains the original output row;
it is stronger than the existence of a central characteristic root.
It does not determine the growth of the invariant at the physical
reset.

## 1. The reflected original source

Let \(a=\sigma 2k\), \(b=-a\), where \(k\ge1\) and
\(\sigma\in\{1,-1\}\). Fix \(N\ge2\),
\(q=e^{\pi i/N}\), and \(Q=q^2\). Use the natural signed clock
and the exact original transfers from the
[two-run source note](research_two_run_source_transfer.md):
\[
 \begin{split}
 T_j(x)&=\mathcal T_a(j;x^\sigma),\\
 A_j(x)&=\mathcal T_a(j;x^\sigma)
                    \otimes\mathcal T_{-a}(j;x^{-\sigma}),\\
 P_a(x)&=T_{N-1}(x)\cdots T_0(x),\qquad
 c^T=e_k^T\otimes e_k^T.
 \end{split}                                                    \tag{1}
\]
For \(|x|=1\), the original signed matrices satisfy
\[
        A_j(x)=T_j(x)\otimes\overline{T_j(x)},\qquad
        U_N(x)=P_a(x)\otimes\overline{P_a(x)}.
 \tag{2}
\]
This conjugation is an equality at the unit clock. Off that circle
the signed-clock matrices are holomorphic Laurent matrices, not
antiholomorphic substitutions.

The augmented original transfer has the product
\[
 \prod_{j=N-1}^{0}
   \begin{pmatrix}A_j(x)&0\\c^TA_j(x)&1\end{pmatrix}
       =\begin{pmatrix}U_N(x)&0\\r_N(x)&1\end{pmatrix}.
 \tag{3}
\]
The product order and the output row in (3) are the literal turn
and cap pairing. In particular no positive replacement of the
source is being introduced.

Suppose \(x_0\) lies on the unit circle and
\[
       P_a(x_0)u_0=\lambda u_0,\qquad
              |\lambda|=1,\quad u_0\ne0.
 \tag{4}
\]
Retain all colors by setting
\[
        u_{j+1}=T_j(x_0)u_j,\quad 0\le j<N.
 \tag{5}
\]
Thus \(u_N=\lambda u_0\). The tensor vectors
\(v_j=u_j\otimes\overline{u_j}\) form an exactly closed cycle:
\(v_N=v_0\), \(v_{j+1}=A_j(x_0)v_j\).
Its marked period is
\[
 \Pi_N(u_0)=\sum_{j=1}^{N}c^Tv_j
             =\sum_{j=1}^{N}|(u_j)_k|^2.
 \tag{6}
\]

## 2. Uniform observability from the original channel equations

**Theorem 1.** Under (4),
\[
 \boxed{\quad
 \Pi_N(u_0)\ \ge\
   \frac{48}{49^k-1}\sum_{j=1}^{N}\|u_j\|_2^2
 \ \ge\ \frac{48}{49^k-1}\|u_0\|_2^2>0.
 \quad}                                                         \tag{7}
\]
The constant depends only on the fixed number of channels. It is
independent of \(N\), the level parity, the power sign, and the
unit clock.

*Proof.* Put \(q_\sigma=q^\sigma\),
\(\xi_j=x_0^\sigma Q^{\sigma j}\), and \(r_j=q_\sigma\xi_j\).
The original even transfer satisfies the exact channel equations
\[
 \begin{split}
 H_ju_{j+1}&=d_ju_j,\\
 H_j&=C_k(r_j)-q_\sigma^{-1}E_{kk},\\
 d_j&=(1-\xi_j)(1-\xi_j^{-1}).
 \end{split}                                                    \tag{8}
\]
They follow from the pole-canceled transfer identity and hold even
at a removable singularity of its initial inverse notation.
No inverse of \(H_j\) or division by \(d_j\) will be used below.
Since \(|\xi_j|=|q_\sigma|=1\),
\[
 0\le d_j\le4,\qquad
 |r_j+r_j^{-1}|\le2,\qquad
 |r_j+r_j^{-1}-q_\sigma^{-1}|\le3.
 \tag{9}
\]

For each channel \(h\), write
\(V_h=((u_1)_h,\ldots,(u_N)_h)\in\mathbb C^N\).
The vector of preceding colors is the unitary shift of \(V_h\)
whose first entry is \(\lambda^{-1}(u_N)_h\).
This is precisely where the unit-modulus condition in (4) is used.

For \(k=1\), the first inequality in (7) is equality.
For \(k\ge2\), the last row of (8) gives
\[
       \|V_{k-1}\|_2\le(3+4)\|V_k\|_2=7\|V_k\|_2.
 \tag{10}
\]
For the subsequent interior rows \(2\le h\le k-1\), the same
equations give
\[
           \|V_{h-1}\|_2\le6\|V_h\|_2+\|V_{h+1}\|_2.
 \tag{11}
\]
Starting at the last row and using \(6+1/7<7\), induction yields
\[
                      \|V_h\|_2\le7^{k-h}\|V_k\|_2.
 \tag{12}
\]
Hence
\[
 \sum_{j=1}^{N}\|u_j\|_2^2
  =\sum_{h=1}^{k}\|V_h\|_2^2
  \le\left(\sum_{h=0}^{k-1}49^h\right)\|V_k\|_2^2.
 \tag{13}
\]
The last norm squared is (6). Finally
\(\|u_N\|_2=\|u_0\|_2\). Equations (13) and (6) prove (7).
\(\square\)

The proof also gives the qualitative assertion directly: if every
last-channel output vanished, the last row of (8) would force
the penultimate channel to vanish at all colors, and then every
earlier channel. The quantitative estimate retains this argument
without any spectral gap or diagonalizability assumption.

## 3. An actual affine pole, including multiple determinant roots

Let \(\mathcal D_{a,-a}(X)\) be the fixed classical denominator
from the [resonant source characteristic theorem](research_resonant_source_monodromy_characteristic.md).
For the present knot closure it satisfies \(\mathcal D_{a,-a}(1)=1\).
The original marked affine row is the rational row
\[
       \mathfrak h_N(x)=r_N(x)(I-U_N(x))^{-1},
       \qquad \det(I-U_N(x))=\mathcal D_{a,-a}(x^N).
 \tag{14}
\]
It is defined generically and extends meromorphically.

**Corollary 2.** If (4) holds, then \(\mathfrak h_N\) has a
nonremovable pole at \(x_0\). If \(x_0^N\) is a simple zero of
\(\mathcal D_{a,-a}\), the pole is simple and its row residue is
nonzero. These assertions hold at every point in the finite clock
orbit of \(x_0\).

*Proof.* The tensor cycle in (5) satisfies
\(U_N(x_0)v_0=v_0\). Multiplication of the original augmented
matrices gives
\[
                         r_N(x_0)v_0=\Pi_N(u_0)>0.
 \tag{15}
\]
If \(\mathfrak h_N\) were holomorphic at \(x_0\), the rational
identity
\(\mathfrak h_N(I-U_N)=r_N\) could be evaluated there.
Its contraction with \(v_0\) would make the left side zero and
the right side positive. This contradiction proves that the
meromorphic singularity is nonremovable. It requires no
simple-root or semisimple-eigenvalue hypothesis.

At a simple denominator zero the adjugate formula gives at most
a simple pole, so its nonremovability makes the residue nonzero.
This is also the marked-period criterion in Proposition 4 of
the [Laurent numerator note](research_two_run_marked_laurent_numerator.md).
Since \(x_0^N\ne1\), every original color transfer is invertible
on this clock orbit. The affine equation then propagates
removability, or nonremovability, around the orbit. \(\square\)

To apply the corollary, it is enough that
\(T_{2k}^{\mathrm{cl}}(X^\sigma)\) have a unit-modulus eigenvalue
at \(|X|=1\). For every \(x_0^N=X\), the proved characteristic
identity gives a unit-modulus eigenvalue of \(P_a(x_0)\), with
the recorded factor \((-1)^N\). A corresponding nonzero
eigenvector exists without a diagonalizability assumption.
Theorem 1 and Corollary 2 then apply to the actual marked row.

There is a direct one-channel check at every level. Take \(a=2\),
\(b=-2\), \(\theta=\pi/3\), and \(x_0=e^{i\theta/N}\). Then
\[
 A_j(x_0)=2-Q^jx_0-(Q^jx_0)^{-1}
       =4\sin^2\!\left(\frac{\theta+2\pi j}{2N}\right)>0.
 \tag{16}
\]
Their product is \(2-e^{i\theta}-e^{-i\theta}=1\).
Thus
\[
 r_N(x_0)=\sum_{j=0}^{N-1}\prod_{h=0}^{j}A_h(x_0)\ge1,
 \qquad
 \mathcal D_{2,-2}(X)=X+X^{-1}-1.
 \tag{17}
\]
The root \(X=e^{i\pi/3}\) is simple, and the exact nonzero residue is
\[
 \operatorname{Res}_{x=x_0}\mathfrak h_N(x)
       =\frac{r_N(x_0)}
          {N x_0^{N-1}(1-e^{-2\pi i/3})}.
 \tag{18}
\]
This example checks the original affine normalization at both
level parities without an eigenvector normalization choice.

This conclusion concerns its auxiliary clock singularities. It
does not estimate the source at \(x=1\), the coherent scalar
\(\kappa^{a-a}\zeta_D\), or its hyperbolic exponential rate.
It also does not assert a physical free-boundary singularity:
the auxiliary clock here is not the geometric boundary angle.

## 4. Existence for every even run length

The unit-modulus hypothesis needed above always occurs at a
nontrivial unit clock. This assertion does not require selection
of an eigenvalue branch or simplicity of a determinant root.

**Theorem 3.** For every \(k\ge1\), there is
\(\theta_k\in(0,\pi)\) such that
\[
       \rho\!\left(T_{2k}^{\mathrm{cl}}(e^{i\theta_k})\right)=1,
 \qquad
       \rho\!\left(T_{2k}^{\mathrm{cl}}(e^{i\theta})\right)<1
                       \quad(0\le\theta<\theta_k).
 \tag{19}
\]
Here \(\rho\) denotes spectral radius. For every \(N\ge2\) and
\(\sigma\in\{1,-1\}\), the actual reflected source with
\(a=\sigma2k,\ b=-a\) has a nonremovable affine pole at
\[
                 x_N=\exp(i\sigma\theta_k/N).
 \tag{20}
\]
It also has a nonremovable pole at each point of the two
disjoint clock orbits of \(x_N\) and \(\overline{x_N}\).
In particular there are at least \(2N\) distinct such poles.

*Proof.* The pole-canceled classical even transfer is a polynomial
matrix, with
\[
 T_{2k}^{\mathrm{cl}}(1)=0,\qquad
 T_{2k}^{\mathrm{cl}}(-1)
       =4\,[C_k(-1)-E_{kk}]^{-1}.
 \tag{21}
\]
We verify that the latter inverse exists and has spectral radius
greater than one. Put
\[
 H=C_k(-1)-E_{kk},\qquad B=-H
       =2I_k+T_k-E_{11}+E_{kk},\qquad
 S=\operatorname{diag}(1,-1,\ldots,(-1)^{k-1}),
 \tag{22}
\]
where \(T_k\) is path adjacency. Direct expansion gives
\[
       u^*SBSu
          =\sum_{j=1}^{k-1}|u_j-u_{j+1}|^2+2|u_k|^2.
 \tag{23}
\]
The sum is empty when \(k=1\), in which case \(B=2\).
For every \(k\), (23) is strictly positive on nonzero vectors:
zero successive differences make the vector constant, and the
last term then makes it zero. Thus \(H\) is real symmetric
negative definite. The Rayleigh quotient of the first basis
vector is two for \(k=1\), and one for \(k\ge2\). Consequently
\[
 \rho(T_{2k}^{\mathrm{cl}}(-1))
      =\frac{4}{\lambda_{\min}(B)}
      \ge2>1.
 \tag{24}
\]
There is in fact a lower bound four for \(k\ge2\).

The spectral radius is continuous in the entries of a finite
matrix, including at repeated eigenvalues. Therefore
\(f_k(\theta)=\rho(T_{2k}^{\mathrm{cl}}(e^{i\theta}))\)
is continuous on \([0,\pi]\), with \(f_k(0)=0\) and
\(f_k(\pi)\ge2\). The first point of the closed set
\(\{\theta:f_k(\theta)\ge1\}\) lies strictly between zero
and \(\pi\), has value one, and proves (19). At that point
some eigenvalue has modulus one. No continuous individual
eigenvalue labeling has been used.

For (20), the first run's natural signed clock has
\(x_N^{N\sigma}=e^{i\theta_k}\). The exact characteristic
identity in Section 3 therefore gives a unit-modulus eigenvalue
of its original quantum monodromy, for both level parities.
Theorem 1 and Corollary 2 give the actual nonremovable pole.
The classical transfer has real coefficients, so conjugating
\(e^{i\theta_k}\) supplies another unit-modulus eigenvalue and
the conjugate pole. The two classical clocks are distinct
because \(0<\theta_k<\pi\). Their \(N\)-th-root orbits are
therefore disjoint, and Corollary 2 propagates the poles around
both orbits. This proves the last assertion. \(\square\)

The pole nearest the chosen reset direction satisfies the explicit
bound
\[
       |x_N-1|=2\sin\!\left(\frac{\theta_k}{2N}\right)
                    \le\frac{\theta_k}{N}<\frac{\pi}{N}.
 \tag{25}
\]
Thus this family of original affine rows has no common fixed
holomorphic disk about the auxiliary clock \(x=1\) as \(N\)
increases. The statement is solely about this auxiliary clock.
It neither produces a singularity of the original geometric
boundary packet nor evaluates the invariant at the reset.

For the one-channel case, equations (16)--(18) give the exact
choice \(\theta_1=\pi/3\) and its nonzero simple residue.
The path energy argument (21)--(24) proves existence for every
fixed number of channels.
