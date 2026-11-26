# Separate endpoint cofactors: an exact all-real-face test at level eight

The all-level question is whether the two actual even cofactors
\(D=R_{m-1}\) and \(T=R_m\) are separately real stable. The
five-term decomposition would then be a finite signed expansion
into stable pieces. This note proves the full real-face
hyperbolicity test at \(N=8\), not merely a test at positive or equal
outer faces. It does not prove the all-level assertion or its source
rate consequences.

## 1. Keep the original recurrence and all real face directions

Set \(N=8\), \(m=4\), and write

\[
r=\sqrt2,\quad u=\sqrt{2+r},\quad w=ru=\sqrt{4+2r},
\quad v=u^3-3u=\sqrt{2-r}.
\tag{1}
\]

The exact original sine and diagonal lists are

\[
(s_1,s_2,s_3,s_4)=(v,r,u,2),\qquad
(a_0,a_1,a_2,a_3)=(2+u,2+v,2-v,2-u).
\tag{2}
\]

Introduce the real coordinates \(A=x+y\), \(B=x-y\), so
\(xy=(A^2-B^2)/4\). Every real pair \((x,y)\) corresponds to
one real pair \((A,B)\), including opposite signs. Starting with
\(R_0=1\), use exactly

\[
R_j=b^j\prod_{k<j}a_k+s_j^2 A R_{j-1}
       +s_js_{j-1}a_{j-1}\frac{A^2-B^2}{4}R_{j-2}.
\tag{3}
\]

The polynomials of interest are \(D=R_3\) and \(T=R_4\). Their
leading coefficients in \(b\) are positive constants independent
of \(A,B\).

## 2. Exact discriminants

For a four-entry row \(q=(q_0,q_1,q_2,q_3)\), put
\(\langle q\rangle=q_0+q_1r+q_2u+q_3w\).
Expansion of the exact recurrence and the polynomial discriminant
gives

\[
\operatorname{disc}_bR_j
=\sum_{k=0}^{j(j-1)/2}\langle q_{j,k}\rangle
 A^{j(j-1)-2k}B^{2k},\qquad j=3,4,
\tag{4}
\]

with the following integer rows. No positive scalar normalization
has been removed from these discriminants.

| \(j\) | \(k\) | \(q_0\) | \(q_1\) | \(q_2\) | \(q_3\) |
| --- | --- | ---: | ---: | ---: | ---: |
| 3 | 0 | 536 | 448 | 374 | 190 |
| 3 | 1 | 2162 | 1665 | 1206 | 894 |
| 3 | 2 | 1300 | 1230 | 562 | 778 |
| 3 | 3 | 354 | 305 | 162 | 186 |
| 4 | 0 | 375223552 | 265705480 | 202764800 | 143972688 |
| 4 | 1 | 1973513088 | 1397423840 | 1066621536 | 756964704 |
| 4 | 2 | 727401568 | 517412200 | 391233312 | 280823152 |
| 4 | 3 | 104318848 | 75412736 | 54817728 | 40985152 |
| 4 | 4 | 766272 | 828248 | 46144 | 423728 |
| 4 | 5 | 24064 | 14880 | -12320 | -5536 |
| 4 | 6 | 1120 | 312 | -864 | 16 |

Every coefficient in (4) is strictly positive. Only the last two
rows require an estimate. The rational bounds

\[
\frac{707}{500}<r<\frac{283}{200},\quad
\frac{1847}{1000}<u<\frac{231}{125},\quad
\frac{2613}{1000}<w<\frac{1307}{500}
\tag{5}
\]

follow by squaring, first for \(r\), then for \(u^2=2+r\) and
\(w^2=4+2r\). Substitution of the lower endpoint for a positive
coefficient and the upper endpoint for a negative coefficient
in the last two rows proves strict positivity using rational
arithmetic. Thus the discriminants are nonzero at every
\((A,B)\ne(0,0)\).

The companion exact script constructs (3) in
\(\mathbb Q(\sqrt{2+\sqrt2})\), computes both discriminants, and
compares every coefficient with (4). It also verifies (5) and its
strict lower bounds with rational arithmetic. It performs no
numerical root sampling.

## 3. Count all roots at one base point, then continue

At \(A=0,B=1\), the cubic has the form

\[
R_3(b)=a_0a_1a_2 b^3
       -\frac{s_3s_2a_2a_0}{4}b.
\tag{6}
\]

All displayed constants are positive. Therefore its three roots
are real and distinct. At the same point the quartic is

\[
\begin{aligned}
R_4(b)&=2b^4+\beta b^2+\gamma,\\
\beta&=1-r-2u+w<0,\\
\gamma&=1-r/4-u+w/2>0,\\
\beta^2-8\gamma&=2w-2r-1>0.
\end{aligned}
\tag{7}
\]

The signs follow directly from (5); the sign of \(\beta\) and
\(\gamma\) can also be read from the alternating dimer terms
in (3). The quadratic in \(b^2\) has two distinct positive roots,
so the quartic has four distinct real roots.

The punctured real parameter plane \(\mathbb R^2\setminus\{0\}\)
is connected. Along any path in it, the degree in \(b\) cannot
drop because the leading coefficient is a fixed positive constant.
The real roots cannot leave the real line without colliding, and
(4) excludes every collision. Consequently \(R_3\) and \(R_4\)
have respectively three and four real simple \(b\)-roots for
every real \((A,B)\ne(0,0)\). At the origin they are positive
scalar multiples of \(b^3\) and \(b^4\).

This proves strict hyperbolicity in the \(b\) direction, with the
usual homogeneous exception at the origin. The polynomials have
nonnegative coefficients in the original variables \((b,x,y)\)
by (3) before the \((A,B)\) substitution. Thus the usual
hyperbolicity-cone characterization also gives separate real
stability: the entire positive orthant lies in the nonvanishing
component containing the positive \(b\) axis. If that standard
characterization is not taken as an input, the conclusion verified
directly here is the complete all-real-face hyperbolicity statement,
not an explicitly constructed PSD determinant.

## 4. What remains open

This calculation does not justify extrapolation in \(N\). No
degree-independent discriminant formula, no general hyperbolicity
proof, and no PSD pencil for the actual even \(R_{m-1}\) or
\(R_m\) has been obtained. The positive q-Hahn determinant in the
existing source notes identifies a cofactor at its complete spectral
node; the actual endpoint \(-2\) at even level is off that node.
The known coefficientwise comparison does not establish stability.

There is also no common principal-minor construction for this pair
even at \(N=6\). With \(x=y=1\) and \(r=\sqrt3\), the actual pair is

\[
\begin{aligned}
D&=2(2+r)b^2+6(2+r)b+12+2r,\\
T&=2\{b^3+(16+8r)b^2+(48+25r)b+42+12r\}.
\end{aligned}
\tag{8}
\]

Its real combination has

\[
\operatorname{disc}_b(D-T/10)
=\frac4{625}(-3021+131\sqrt3)<0.
\tag{9}
\]

Hence an auxiliary polynomial \(D+tT\), or equivalently
\(T+tD\), cannot be jointly real stable. In particular one cannot
realize \(D\) as the principal cofactor of a positive Hermitian
bordered pencil realizing \(T\). This is consistent with separate
stability and does not obstruct a five-term expansion using two
different stable realizations.

The precise remaining parity task is therefore still separate
all-level stability, followed by an actual rate comparison for the
five extracted terms, including their monomial target shifts.
Neither conclusion follows from the level-eight calculation.

## 5. Reproduction and source scope

The exact finite certificate is
`md-even-dt-n8-exact-certificate.py`, with its adjacent JSON output.
It uses only SymPy's exact rational/algebraic polynomial operations.
The source recurrence is the one in
`actual_cross_cofactor_factorization.md` Sections 1–2. The original
level, all face variables, and the polynomial scalars are retained.
The other source files read were
`actual_q_hahn_boundary_model_curvature.md`,
`actual_q_hahn_joint_accretive_determinant.md`, and
`actual_q_hahn_full_physical_complex_packet.md`.
Their positive Hermitian claims are used only to delimit the existing
complete-node input, not as an off-node stability proof.
