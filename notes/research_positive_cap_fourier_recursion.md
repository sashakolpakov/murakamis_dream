# Exact Fourier recursion for the original positive cap moments

Research note, 3 November 2026. Frozen manuscripts are unchanged.

This note gives an exact scalar-polynomial evolution for every fixed
positive three-crossing cap chain. Its initial datum is the original
cap, and both polynomial projections are retained. A tridiagonal clock
intertwiner follows because its apparent endpoint current cancels
exactly. A separate positive reduction replaces the original cap
vectors by powers of a skew-crossing Gram matrix with exponentially
small relative error. These statements do not determine the sharp
moment rate beyond the third moment.

## 1. A finite Fourier factorization

Use the original crossing \(M\) and notation of
[the positive-cycle theorem](research_positive_three_crossing_cycle.md):
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=q^{D^2/2},\quad
 F_j=(Q;Q)_j,\quad S_j=|F_j|,\quad H=M^*M .
 \tag{1}
\]
The mirrored crossing has the conjugate formulas throughout.
All matrices below have the original \(N\) coordinates, including
the normal directions at the repeated physical roots. Put
\[
 a_j=\frac{(-q)^j}{F_j},\qquad
 b_j=\frac{q^{j^2}}{F_j}=\overline{a_j},\qquad
 A(z)=\sum_{j=0}^D a_jz^j,\qquad
 B(z)=\sum_{j=0}^D b_jz^j .
 \tag{2}
\]
Let \(U_{ij}=N^{-1/2}Q^{ij}\) be the unitary Fourier matrix, and let
\(D_{\rm row}=\operatorname{diag}(\kappa(-q)^i)\).

**Theorem 1.** The upper triangular matrix
\[
 C_{\ell j}=
 \begin{cases}a_\ell b_{j-\ell},&\ell\le j,\\0,&\ell>j,\end{cases}
 \qquad
 C=\operatorname{diag}(a_\ell)B(S),
 \tag{3}
\]
where \(S_{j,j+1}=1\), satisfies
\[
                  M=\sqrt N\,D_{\rm row}UC,\qquad
                  H=NC^*C,\qquad
                  A(S)B(S)=I .
 \tag{4}
\]
In particular \(H\) retains the exact original positive cap measure.

*Proof.* The original crossing formula is
\[
 M_{ij}=\kappa(-q)^i q^{j^2}
       \frac{(Q^{1-j}Q^i;Q)_j}{F_j}.
 \tag{5}
\]
For \(i<j\) the numerator is zero, so (5) holds on the full square.
The finite \(q\)-binomial identity gives
\[
 [z^\ell]\left\{q^{j^2}
       \frac{(Q^{1-j}z;Q)_j}{F_j}\right\}
  =\frac{(-1)^\ell q^{(j-\ell)^2+\ell}}
          {F_\ell F_{j-\ell}}
  =a_\ell b_{j-\ell}.
 \tag{6}
\]
Evaluation at the \(N\) Fourier roots proves the first identity (4);
unitarity proves the second. The coefficient recurrences
\((1-Q^j)a_j=-qa_{j-1}\) and
\((1-Q^j)b_j=qQ^{j-1}b_{j-1}\) give
\[
 A(Qz)=(1+qz)A(z)-qa_Dz^N,\qquad
 B(Q^{-1}z)=(1+q^{-1}z)B(z)-q^{-1}b_Dz^N .
 \tag{7}
\]
Below degree \(N\), the product \(AB\) is \(Q\)-invariant and has
constant coefficient one. Hence \(AB=1\bmod z^N\).
Since \(S^N=0\), this proves the last identity (4). \(\square\)

Equivalently the full Gram kernel has the single-coefficient formula
\[
 H_{jk}=\frac{Nq^{j^2+k^2}}{F_jF_k}
 [z^j](Q^{1-j}z;Q)_j(Q^{1-k}z;Q)_k .
 \tag{8}
\]
Indeed conjugating the first factor in (5) on the unit circle
reverses its degree-\(j\) polynomial. The Fourier sum then extracts
degree \(j\); the other possible exponents lie strictly between
\(-N\) and \(N\), so there is no alias term. Formula (8) is not
an assertion of entrywise positivity.

## 2. The endpoint current cancels in the clock equation

Let
\[
 X=\operatorname{diag}(Q^j),\qquad
 K=S^T(I-QX)=(I-X)S^T,\qquad
 Y=(I+q^{-1}S)X .
 \tag{9}
\]
The nilpotent shifts satisfy, including their first and last rows,
\[
 SK=I-QX,\qquad KS=I-X,\qquad
 [S^r,K]=(1-Q^r)XS^{r-1}.
 \tag{10}
\]

**Theorem 2.** The following identity holds in the full finite space:
\[
 XH=H\mathcal L,\qquad
 \mathcal L=Y-q^{-1}(K-qX)(I-QY).
 \tag{11}
\]
In particular \(\mathcal L=H^{-1}XH\) is tridiagonal, with entries
\[
 \begin{split}
 \mathcal L_{jj}&=3Q^j-(1+Q)Q^{2j},\\
 \mathcal L_{j,j+1}&=qQ^j(1-Q^{j+1})\quad(j<D),\\
 \mathcal L_{j,j-1}&=-q^{-1}(1-Q^j)^2\quad(j>0).
 \end{split}
 \tag{12}
\]
There is no omitted corner row in this identity.

*Proof.* Write \(T=B(S)\). Equations (7) and (10) imply
\[
 T^{-1}XT=Y,\qquad
 T^{-1}KT=K-qX+q^{-1}b_DS^D .
 \tag{13}
\]
For the second identity, expand \([T,K]\) by (10).
The infinite-series term would be \(qXB(QS)\); the absent degree
\(N\) coefficient contributes precisely \(q^{-1}b_DS^D\)
after multiplication by \(T^{-1}\). Thus it cannot be discarded
before the next calculation.
The diagonal in (3) gives
\[
 C^{-1}XC=Y,\qquad
 (C^*)^{-1}XC^*=X+K,\qquad
 C^{-1}KC=-q^{-1}
 (K-qX+q^{-1}b_DS^D)(I-QY).
 \tag{14}
\]
The last row of \(Y\) is \(Q^De_D^T\), so
\[
                         S^D(I-QY)=0 .
 \tag{15}
\]
Substituting (14) into \(H^{-1}XH=C^{-1}(X+K)C\)
proves (11). Multiplication of the two bidiagonal factors gives
(12). \(\square\)

The first column is fixed, including its scale:
\[
                He_0=N(a_0,\ldots,a_D)^T .
 \tag{16}
\]
It is the unique solution of
\((\mathcal L^*-I)f=0,\ f_0=N\).
Uniqueness follows successively from the nonzero superdiagonal
of \(\mathcal L^*\). More generally (11), the first column
(16), and the nonzero subdiagonal of \(\mathcal L\) determine
every row of \(H\) by a three-term polynomial recurrence.
This is a local difference equation for the actual kernel, not
an assumed asymptotic eigenvector.

## 3. A cap-initialized polynomial evolution and its positive energy

Write \(\Pi_+\) for the nonnegative-power part of a Laurent
polynomial and \(\Pi_{<N}\) for truncation to degrees \(0,\ldots,D\).
Define the diagonal coefficient operator
\[
 \mathcal W\!\left(\sum_{j=0}^D g_jz^j\right)
       =\sum_{j=0}^D S_j^{-2}g_jz^j .
 \tag{17}
\]
For \(f^{(r)}=H^re_0\), let \(F_r(z)=\sum_j f^{(r)}_jz^j\).
Then the full original source obeys the exact iteration
\[
 \begin{split}
 F_0(z)&=1,\\
 G_r(z)&=\Pi_+\!\left[B(z^{-1})F_r(z)\right],\\
 F_{r+1}(z)&=N\Pi_{<N}\!\left[A(z)\mathcal W G_r(z)\right].
 \end{split}
 \tag{18}
\]
In coefficients \(g^{(r)}_\ell=\sum_{j=\ell}^D
b_{j-\ell}f^{(r)}_j\). The two projections in (18) retain the
literal finite endpoints. For example \(G_0=1\) and \(F_1=NA\),
with no unknown normalization.

**Proposition 3.** For every \(r\ge0\),
\[
 \mu_{2r,N}=\sum_{j=0}^D|f^{(r)}_j|^2,\qquad
 \mu_{2r+1,N}=N\sum_{\ell=0}^D
                         S_\ell^{-2}|g^{(r)}_\ell|^2 .
 \tag{19}
\]
Thus (18) is a uniform exact algorithm for all fixed-length
original cap moments, and (19) is a positive energy formula for
its intermediate output.

*Proof.* The first equality is \(H=H^*\). The second follows from
\(H=NC^*C\) and \((Cf^{(r)})_\ell=a_\ell g^{(r)}_\ell\).
Expansion of \(C^*C\) gives (18). \(\square\)

For clarity, the projection currents are explicit Laurent
polynomials, not errors:
\[
 \begin{split}
 B(z^{-1})F_r(z)&=G_r(z)+R_r^-(z),
                   &\deg_{\max}R_r^-&\le-1,\\
 A(z)\mathcal W G_r(z)&=N^{-1}F_{r+1}(z)+z^NR_r^+(z),
                   &\deg R_r^+&\le N-2 .
 \end{split}
 \tag{20}
\]
They can be computed at each step from the same finite
convolutions. There is also a useful exact clock formulation.
Set \((\mathcal T F)(z)=F(Qz)\),
\(\mathcal B F=\Pi_+[B(z^{-1})F]\), and
\(\mathcal A G=\Pi_{<N}[A(z)G]\). Then
\[
 \begin{split}
 z(\mathcal BF)(Qz)
   &=(z+q^{-1})(\mathcal B\mathcal TF)(z)
           -q^{-1}(\mathcal B\mathcal TF)(0),\\
 (\mathcal AG)(Qz)
   &=(1+qz)(\mathcal A\mathcal TG)(z)
           -q[z^D](\mathcal A\mathcal TG)\,z^N,\\
 (2-\mathcal T-\mathcal T^{-1})\mathcal WG
   &=z\,\mathcal W\!\left(\frac{G-G(0)}z\right).
 \end{split}
 \tag{21}
\]
These follow from (7) and \(S_j^2/S_{j-1}^2
=2-Q^j-Q^{-j}\). The constant and degree-\(N\) terms in
(21) are the actual projection corrections. Equation (21)
does not assert a bounded-degree scalar annihilator for
arbitrary many iterations.

## 4. An exponentially accurate positive reduction for every fixed length

Let \(\mathsf D=M-M^T\) and
\[
 \mathsf W=\mathsf D^*\mathsf D
           =H+H^{-1}-2I\ge0,\qquad
 \tau_{m,N}=e_0^*\mathsf W^m e_0 .
 \tag{22}
\]
The matrix \(\mathsf W\) is unrelated to the coefficient multiplier
\(\mathcal W\) in (17). The equality in (22) uses
\((M^*)^{-1}=M^T\). In particular the replacement below uses only
the original crossings and their transpose.

**Theorem 4.** For every integer \(m\ge0\),
\[
       \boxed{\quad
       \mu_{m,N}=\sum_{k=0}^m {m+k\choose 2k}\tau_{k,N}.
       \quad}
 \tag{23}
\]
Let \(c,v,C_2,C_3\) be the proved cap-seed constants in
[the third-moment theorem](research_positive_three_crossing_cap_seed.md),
so \(\mu_2\sim C_2N^{3/2}e^{Nc}\),
\(\mu_3\sim C_3N^{3/2}e^{Nv}\), and \(v>2c>0\).
For each fixed \(m\ge3\),
\[
 \mu_{m,N}=\tau_{m,N}
                   \left[1+O_m(e^{-N(v-c)})\right].
 \tag{24}
\]
For each fixed \(r\ge2\), the actual cap vectors satisfy
\[
 \frac{\|H^re_0-\mathsf W^re_0\|}
      {\|H^re_0\|}
       =O_r(e^{-N(v-c)/2}).
 \tag{25}
\]
For \(r=1\) their difference has squared norm exactly \(N\);
its relative norm is \(O(N^{-1/4}e^{-Nc/2})\).

*Proof.* The positive-cycle theorem proves the exact reciprocal
cap identity
\(\mu_{-j,N}=\mu_{j-1,N}\) for \(j\ge1\).
Let \(P_0(y)=1,\ P_1(y)=y-1\), and
\(P_m=yP_{m-1}-P_{m-2}\).
For \(x\ne0\),
\[
 P_m(x+x^{-1})
  =x^m+\sum_{j=0}^{m-1}(-1)^{m-j}
                                      (x^j-x^{-j-1}).
 \tag{26}
\]
Taking the original cap expectation eliminates every term of
the sum. Also
\[
 \sum_{m\ge0}P_m(2+w)t^m
   =\frac{1-t}{(1-t)^2-wt}
   =\sum_{k\ge0}\frac{w^kt^k}{(1-t)^{2k+1}} .
 \tag{27}
\]
Coefficient comparison proves (23).
In particular
\[
 \tau_1=N-1,\quad
 \tau_2=\mu_2-3N+2,\quad
 \tau_3=\mu_3-5\mu_2+9N-5 .
 \tag{28}
\]
Hence \(\tau_2\sim\mu_2\), \(\tau_3\sim\mu_3\), and
\(\tau_2/\tau_3=O(e^{-N(v-c)})\).
The nonnegative \(\mathsf W\)-spectral measure has increasing
moment ratios. For every fixed \(m\ge3\), all lower moments in
(23) are at most a constant times \(\tau_{m-1}\) for large \(N\),
and \(\tau_{m-1}/\tau_m\le\tau_2/\tau_3\).
This proves (24), with nonnegative relative error.

For \(x\ge1\),
\[
 0\le x^r-(x+x^{-1}-2)^r
       =x^r[1-(1-x^{-1})^{2r}]\le2r x^{r-1}.
 \tag{29}
\]
For \(0<x\le1\), its absolute value is at most \(2x^{-r}\).
Functional calculus and reciprocal cap moments therefore give
\[
 \|H^re_0-\mathsf W^re_0\|^2
 \le4r^2\mu_{2r-2,N}+4\mu_{-2r,N}
 \le4(r^2+1)\mu_{2r-1,N}.
 \tag{30}
\]
The last inequality uses increasing nonnegative moment ratios,
starting with \(\mu_1=N\ge\mu_0=1\).
For \(r\ge2\),
\(\mu_{2r-1}/\mu_{2r}\le\mu_2/\mu_3
=O(e^{-N(v-c)})\), proving (25).
When \(r=1\), \(H-\mathsf W=2I-H^{-1}\), so its cap squared norm
is \(4\mu_0-4\mu_{-1}+\mu_{-2}=N\). \(\square\)

This is a relative estimate for the actual cap sequence, despite
the fact that \(H-\mathsf W=2I-H^{-1}\) is not small in operator
norm. It removes a reciprocal spectral contribution without
assuming a dominant cap eigenvector or a prepared Gaussian.
It does not replace the convolution in (18) by its absolute
values. Determining the sharp rate of its weighted positive
energy for general fixed \(r\) remains the source problem.
The exact capped words and their distinction from a topologically
identified knot invariant are those in the positive-cycle and
cap-seed notes.

## 5. Reversal parity retains both cap contributions

Let \(h=\lfloor N/2\rfloor\), and use the real orthonormal vectors
\[
 p_j^\pm=\frac{e_j\pm e_{D-j}}{\sqrt2}\quad(0\le j<h).
 \tag{31}
\]
For odd \(N=2h+1\), add \(e_h\) to the plus basis. Denote the
resulting isometries by \(P_+\) and \(P_-\).
Since \(J\mathsf D J=-\mathsf D\) and
\(\mathsf D^T=-\mathsf D\), in this basis one has exactly
\[
 \mathsf D=
 \begin{pmatrix}0&B\\-B^T&0\end{pmatrix},\qquad
 \mathsf W=
 \begin{pmatrix}\overline B B^T&0\\0&B^*B\end{pmatrix}
                  =\begin{pmatrix}W_+&0\\0&W_-\end{pmatrix}.
 \tag{32}
\]
The block \(B\) has \(N-h\) rows and \(h\) columns. Its entries
are still original crossing entries:
\[
 B_{jk}=\mathsf D_{jk}+M_{D-k,j}\quad(j,k<h),\qquad
 B_{hk}=\sqrt2\,M_{hk}\quad(N=2h+1).
 \tag{33}
\]
The two blocks have identical nonzero spectra; in odd dimension
the plus block has at least one exact zero eigenvalue.

**Proposition 5.** For every fixed \(m\ge3\), each normalized
parity cap has the full leading cap moment:
\[
 (p_0^\pm)^*\mathsf W^m p_0^\pm
       =\tau_{m,N}\left[1+O_m(e^{-N(v-c)/2})\right].
 \tag{34}
\]
For \(m=2\) the relative error is
\(O(N^{-1/4}e^{-Nc/2})\).
Thus the original decomposition
\(e_0=(p_0^++p_0^-)/\sqrt2\) shares its positive energy
equally, to exponential accuracy, between the two parities.

*Proof.* The commutation \(J\mathsf W=\mathsf WJ\) makes
\(\nu_m=e_0^*\mathsf W^me_D\) real and gives the exact identity
\[
 (p_0^\pm)^*\mathsf W^mp_0^\pm=\tau_{m,N}\pm\nu_m .
 \tag{35}
\]
For \(k\ge1\), positive functional calculus and reciprocity give
\[
 |e_0^*H^ke_D|
 \le\sqrt{\mu_{k,N}\,e_D^*H^ke_D}
 =\sqrt{\mu_{k,N}\mu_{k-1,N}}.
 \tag{36}
\]
Negative \(k\) give the conjugate corner entry. The coefficients
of \((x+x^{-1}-2)^m\) have absolute sum at most \(4^m\);
its constant term contributes zero to the opposite-corner entry.
Increasing positive moments therefore imply
\[
                    |\nu_m|\le4^m
                         \sqrt{\mu_{m,N}\mu_{m-1,N}} .
 \tag{37}
\]
For \(m\ge3\), (24) and
\(\mu_{m-1}/\mu_m\le\mu_2/\mu_3\) prove (34).
For \(m=2\), use \(\tau_2\sim\mu_2\) and
\(\mu_1/\mu_2=O(N^{-1/2}e^{-Nc})\).
\(\square\)

Parity does not turn these Gram matrices into a real weighted
Dirichlet matrix by a diagonal phase or amplitude change.
The next assertion rules out that specific proposed lower-bound
mechanism; it does not rule out a different positive quadratic form.

**Proposition 6.** At every \(N\ge64\), each block \(W_\pm\) has
a nonreal three-entry cycle:
\[
             \Im\bigl((W_\pm)_{01}(W_\pm)_{12}
                                      (W_\pm)_{20}\bigr)<0 .
 \tag{38}
\]
For the mirrored crossing the sign is reversed.
Consequently no nonsingular complex diagonal similarity, or
diagonal Hermitian congruence, makes either block real
entrywise. In particular diagonal phases and positive diagonal
weights do not produce an entrywise-positive or real Dirichlet
matrix in these parity coordinates.

*Proof.* For the first three indices the block entries are
\[
 (W_\pm)_{jk}=H_{jk}+H_{D-j,D-k}
                       \pm(H_{j,D-k}+H_{D-j,k})
                       \quad(j\ne k,\ j,k\le2).
 \tag{39}
\]
For \(r,j,k\le2\), the original sine-factorial formula and
\(S_{D-r}=N/S_r\) give
\[
 |M_{D-r,j}|\le {r+j\choose j},\qquad
 |M_{D-r,D-k}|\le {k\choose r}\quad(r\le k).
 \tag{40}
\]
Indeed the relevant ratios are the absolute values of the
Gaussian binomials \({r+j\brack j}_Q\) and
\({k\brack r}_Q\). Their polynomials in \(Q\) have nonnegative
integer coefficients, so on \(|Q|=1\) they are bounded by
the corresponding ordinary binomials. Summing the finitely many
nonzero terms in these high columns gives
\[
 \begin{split}
 |H_{D-j,D-k}|&\le {j+k\choose j},\\
 |H_{j,D-k}|&\le
              \sum_{r=0}^k{r+j\choose j}{k\choose r}.
 \end{split}
 \tag{41}
\]
It follows that the corrections to \(H_{01},H_{12},H_{20}\)
in (39) have magnitudes at most \(4,15,6\), respectively.

Write \(s=2\sin(\pi/N)\) and \(c_0=\cos(\pi/N)\), so
\(S_1=s,\ S_2=2s^2c_0\). Formula (4) gives exactly
\[
 H_{01}=\frac{iN}{s},\qquad
 H_{12}=\frac{iN}{s}
                  \left(\frac q{S_2}+\frac1{s^2}\right),
 \qquad H_{20}=-\frac{Nq^{-1}}{S_2}.
 \tag{42}
\]
In particular
\[
 -\Im(H_{01}H_{12}H_{20})
     =\frac{N^3\sin(\pi/N)}{s^4S_2}
     =\frac{N^3}{4s^5c_0}=:I_N>0 .
 \tag{43}
\]
For \(N\ge64\), \(s<1/10\) and \(c_0>4/5\).
The three entry magnitudes in (42) are bounded by
\(N/s,\ 13N/(8s^3),\ 5N/(8s^2)\).
Expanding the seven correction terms in their product bounds
the relative change by
\[
 \begin{split}
 \frac{|\Delta(H_{01}H_{12}H_{20})|}{I_N}
 \le{}&\frac{65}{4N}+\frac{75s^2}{2N}
       +\frac{39s}{N}+\frac{150s^3}{N^2}\\
     &+\frac{156s^2}{N^2}+\frac{360s^4}{N^2}
       +\frac{1440s^5}{N^3}<\frac13 .
 \end{split}
 \tag{44}
\]
The last comparison follows by substituting \(N=64,\ s=1/10\);
every displayed positive term decreases as \(N\) increases
under these bounds. Thus (38) follows from (43).
A cycle product is unchanged by diagonal similarity, and is
multiplied by the positive scalar
\(|d_0d_1d_2|^2\) by congruence with
\(\operatorname{diag}(d_j)\). A real matrix would have real
cycle products. This proves the obstruction. \(\square\)

The positive splitting (32)--(34) does not strengthen the
known exponential lower rate for \(\mu_m\): it assigns that
same rate to both actual parity caps. Equations (38)--(44)
explain why applying an entrywise positive comparison to one
of these blocks is not justified.

There is a complementary limitation on a uniform coercivity estimate.
Let \(\epsilon_0\) be the first coordinate in either parity space,
and set \(g_\pm=W_\pm\epsilon_0/\|W_\pm\epsilon_0\|\).
These actual vectors lie in the positive spectral subspaces, including
when the odd plus block has a kernel. Equations (28), (34), and the
proved second and third seeds give
\[
 \langle g_\pm,W_\pm g_\pm\rangle
  =\frac{(p_0^\pm)^*\mathsf W^3p_0^\pm}
         {(p_0^\pm)^*\mathsf W^2p_0^\pm}
  =\frac{C_3}{C_2}e^{N(v-c)}(1+O(N^{-1/2})).
 \tag{45}
\]
Any scalar lower bound \(W_\pm\succeq\alpha_N I\) on that
positive spectral subspace must therefore have
\(\limsup N^{-1}\log\alpha_N\le v-c\).
Iterating only this bound from the known second moment supplies
at most the rate \(c+(m-2)(v-c)\), already provided by moment
log-convexity. Equation (45) is not an upper bound on the higher
moments; it identifies why a uniform elliptic floor alone cannot
improve their present lower rate.

## 6. Reproduction and prior scope

The finite check
[check_positive_cap_fourier_recursion.py](../experiments/check_positive_cap_fourier_recursion.py)
uses the independent original quotient construction of \(M\).
It compares (4), (8), (11)--(16), the entire cap vectors in
(18), both positive energies (19), and the moment identity
(23), and the exact parity blocks and cap split, at both
crossing signs. It also checks the rational bound (44).
Its record is
[research-positive-cap-fourier-recursion.json](../repro/results/research-positive-cap-fourier-recursion.json).
At 110 decimal digits it passed 9,108 identities for \(N=2,\ldots,10\),
at both crossing signs, with maximum relative residual below
\(3.85\times10^{-107}\). The record includes the script and direct
project-dependency hashes.
Finite checks supplement the proofs; they do not establish
an unproved asymptotic.

The earlier
[arbitrary-word local-source compiler](research_rational_word_local_source_system.md)
already retains original endpoints for general rational words.
The additional structure here is the exact unitary Fourier
factorization of the positive block, its tridiagonal clock
intertwiner, and its cap-specific positive evolution and relative
reduction. No new general knot-volume or cofiniteness statement
is inferred.
