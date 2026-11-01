# An absolute source sum can exceed volume while its signed sum cancels

The finite source of a marked diagram is a sum over shared face degrees.
Taking the absolute value of each summand loses information: in the
example below, the resulting positive sum grows faster than the complete
augmented volume rate, at every sufficiently large level of either
parity. At the same spectral tuple, the signed sum has a strictly smaller
rate along odd levels.

Both statements concern one genuine source sector of one unchanged
marked diagram. The selected crossing uses its left recurrence-path
piece, and every other crossing uses its central piece. No maximum over
different spectator sectors is used. The spectral value is \(+2\) at the
selected crossing and \(-2\) at every spectator.

The proof first turns a positive, target-balanced triangle table into
actual integer source arrays. It retains the different finite degrees at
even and odd levels. It then combines the known local coefficient
entropy with the exact rational certificate for the
[54-region example](actual_singleton_sector_envelope_obstruction.md).
The final cancellation statement also uses the separately proved
[odd-level signed cap bound](research_cap_uniform_spectral_gap.md).
No estimate for a filled period or knot invariant is inferred from an
absolute-array lower bound.

## 1. The source and its original targets

Fix a finite simple triangulated oriented sphere with a perfect matching
of its dual triangles. Each matched pair is a crossing region. Write
\(R\) for the number of regions, and retain their ordered quartets
\((x_e,b_e,c_e,y_e)\). The outer matching diagonal is \(x_ey_e\);
the two triangle supports are \((x_e,b_e,y_e)\) and
\((x_e,c_e,y_e)\). Choose an original strand edge, meaning an unmatched
edge, as the mark. Its two incident face variables are set to zero.
These are the *protected* variables. The other \(R\) face variables are
ordinary.

The [matched-sphere source construction](research_matched_sphere_morse_source.md),
§§1–6, realizes these data by the original crossing disks and gives one
shared coefficient extraction. At level \(N\ge2\), put
\[
 d=N-1,\qquad \theta=\pi/N,\qquad q_N=e^{i\theta},\qquad
 \chi_N(\sigma)=2T_N(\sigma/2)+2,
 \qquad
 V_N(\sigma)=\chi_N(\sigma)(\sigma I-\Omega)^{-1}.
 \qquad\text{(1)}
\]
Here \(T_N(\cos t)=\cos Nt\), and \(\Omega\) is the original Casimir
matrix in its polynomial source representation. The last expression is
a matrix polynomial: the scalar factor removes the resolvent poles with
their original multiplicities. We use this full numerator, including
its finite scalar, rather than a separately normalized spectral
projector.

Partition its downward paths into central, left and right pieces,
denoted \(C,L,R\). If a path has input row \(j\) and output row \(i\),
its middle monomial is \(L_b^iL_c^{d-j}\). For \(N=2m\), central paths
have \(i\le m-1\), \(j\ge m\); left paths have \(j\le m-1\), and right
paths have \(i\ge m\). For \(N=2m+1\), central paths have \(i\le m\le j\);
left paths have \(j\le m-1\), and right paths have \(i\ge m+1\).
The exact finite factorization is proved in
[the cofactor calculation](actual_cross_cofactor_factorization.md), §§1–2.

For a fixed string \(\boldsymbol s=(s_e)\), write the local polynomials
after the protected substitutions as
\[
 H_{e,s_e}(\boldsymbol L;\sigma_e)
   =\sum_{\substack{v_e\ge0\\|v_e|=d}}
          a_{e,N}(v_e;\sigma_e)\boldsymbol L^{v_e}.
 \qquad\text{(2)}
\]
Let \(\Gamma_{N,\boldsymbol s}\) consist of the arrays of local exponents
whose sum at every ordinary face is exactly \(d\), with zero at both
protected faces. Unsupported coefficients in (2) are zero. Define
\[
 \begin{aligned}
 A_{\boldsymbol v}(\boldsymbol\sigma)
     &=\prod_e a_{e,N}(v_e;\sigma_e),\\
 S_{N,\boldsymbol s}(\boldsymbol\sigma)
     &=\sum_{\boldsymbol v\in\Gamma_{N,\boldsymbol s}}
                    A_{\boldsymbol v}(\boldsymbol\sigma),\\
 \mathcal A_{N,\boldsymbol s}(\boldsymbol\sigma)
     &=\sum_{\boldsymbol v\in\Gamma_{N,\boldsymbol s}}
                    |A_{\boldsymbol v}(\boldsymbol\sigma)|.
 \end{aligned}
 \qquad\text{(3)}
\]
The second line is the original signed source coefficient. The last
line takes absolute values before the shared summation. All original
targets remain present; no extra marked factor, power of \(N\), or
independent boundary summation is inserted. The original filling
functionals and exterior framing factors have not been applied.

## 2. A general table criterion for an absolute lower bound

Suppose \(s_{e_*}=L\) at one selected region, with every other label
central. Write its ordered quartet as
\[
             (x,b,z,y),\qquad
             b,y\text{ protected},\quad x,z\text{ ordinary}.
 \qquad\text{(4)}
\]
Thus its retained left triangle has just the ordinary corner \(x\);
the overloaded middle is \(z\).

There are \(2(R-1)\) spectator triangles. For each triangle \(t\), let
\(I_t\) be its nonempty ordinary support. Assume numbers
\(\alpha_{tf}>0\), for \(f\in I_t\), and \(0<\lambda<1\) satisfy
\[
 \sum_{f\in I_t}\alpha_{tf}=\frac12,\qquad
 \sum_{t\ni f}\alpha_{tf}
   +\frac{\lambda}{2}\mathbf1_{f=x}
   +\left(1-\frac{\lambda}{2}\right)\mathbf1_{f=z}
       =1
       \quad(f\text{ ordinary}).
 \qquad\text{(5)}
\]
Assume also that the graph on ordinary faces joining two faces whenever
they occur in one spectator triangle is connected. These are conditions
on the original incidences and targets. They do not posit a new
triangulation or a stationary geometric structure for the noncentral
sector.

Use the absolute triangle entropy
\[
 \begin{aligned}
 \Lambda(t)&=-\int_0^t\log|2\sin u|\,du,\\
 f(a)&=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi}
                   \quad(0\le a\le1/2),\\
 E_{\mathrm{tab}}&=\sum_t\sum_{f\in I_t}f(\alpha_{tf}).
 \end{aligned}
 \qquad\text{(6)}
\]
A singleton row has load \(1/2\) and entropy zero.

**Table theorem.** Under these hypotheses, at the fixed real tuple
\[
               \sigma_{e_*}=+2,\qquad
               \sigma_e=-2\quad(e\ne e_*),
 \qquad\text{(7)}
\]
the actual absolute-array sum satisfies
\[
 \boxed{\displaystyle
       \liminf_{N\to\infty}\frac1N
          \log\mathcal A_{N,\boldsymbol s}(\boldsymbol\sigma)
                   \ \ge\ E_{\mathrm{tab}}.}
 \qquad\text{(8)}
\]
The limit in (8) includes both parities. The diagram and table are fixed.
The proof constructs one nonzero array at every sufficiently large
level, not only at levels divisible by a table denominator. Rationality
is useful for certifying (5), but is not needed for the theorem.

## 3. The exact protected coefficient at \(+2\)

Put
\[
 M=\lfloor N/2\rfloor-1,\qquad
 c_r=2\cos((2r+1)\theta),\qquad s_r=2\sin(r\theta),\qquad
 S_j=\prod_{r=1}^j s_r,\qquad
 T_j=\prod_{r=0}^j2\sin((r+1/2)\theta).
 \qquad\text{(9)}
\]
Here \(S_0=1\). At (4), the protected factor \(L_b\) forces \(i=0\),
and the protected outer variable removes every two-step path.
The only surviving path from \(j\) to zero uses \(j\) one-step
\(x\)-factors. Consequently
\[
 [L_x^jL_z^{d-j}]H_{e_*,L}(+2)
        =(-1)^j U_{N,j},\qquad
 U_{N,j}=S_j^2\prod_{r=j+1}^d(2-c_r)
        =4\frac{S_j^2}{T_j^2},
        \qquad 0\le j\le M.
 \qquad\text{(10)}
\]
The unused-row product is the full numerator path formula. The last
identity uses \(\prod_{r=0}^d(2-c_r)=\chi_N(2)=4\); every factor is
nonzero, so no limiting division at a spectral node is involved.

For \(1\le j\le M\),
\[
 \frac{U_{N,j}}{U_{N,j-1}}
     =\frac{\sin^2(j\pi/N)}{\sin^2((j+1/2)\pi/N)}
     \le1.
 \qquad\text{(11)}
\]
All these angles lie in the increasing half of sine. The standard finite
sine products give the following endpoints:
\[
 \begin{array}{c|c|c|c}
 N&M&S_M^2&T_M^2\\ \hline
 2m&m-1&m&2\\
 2m+1&m-1&N/[4\sin^2(m\pi/N)]&1 .
 \end{array}
 \qquad\text{(12)}
\]
For clarity, at odd \(N\) the identity
\(\prod_{r=1}^{N-1}2\sin(r\pi/N)=N\) pairs into \(S_m^2=N\).
The shifted product over \(r=0,\ldots,N-1\) equals \(2\); its middle
factor is \(2\), and its other factors pair, giving \(T_{m-1}^2=1\).
The even products follow by the same pairing. Thus \(U_{N,M}=N\) at
even levels and \(U_{N,M}=N\sec^2(\pi/(2N))\) at odd levels.
Together with (11) and \(\sin t\ge2t/\pi\) on \([0,\pi/2]\), this proves
\[
             N\le U_{N,j}\le
             U_{N,0}=\csc^2(\pi/(2N))\le N^2 .
 \qquad\text{(13)}
\]
The protected coefficient therefore has zero exponential cost,
uniformly over its full left range, at both parities. Its alternating
sign in (10) is not removed.

## 4. Positive spectator factors and their coefficient entropy

Let \(x,b,c,y\) now denote the arguments of an arbitrary spectator.
At \(-2\), multiplication by the common sign \((-1)^d\) makes every
numerator path coefficient nonnegative. This follows because a path
with \(k\) steps has sign \((-1)^k\) and \(d-k\) unused factors of
sign \(-1\). The original endpoint zeros remain in the step weights.

For even \(N=2m\), set \(M=m-1\). Let \(R_M(x,b,y)\) be the original
cleared lower cofactor, defined at level \(N\) by
\[
 \begin{aligned}
 a_r&=2+2\cos((2r+1)\pi/N),\\
 R_0&=1,\\
 R_j(x,b,y)
   &=b^j\prod_{r<j}a_r
       +s_j^2(x+y)R_{j-1}(x,b,y)
       +s_js_{j-1}a_{j-1}xyR_{j-2}(x,b,y).
 \end{aligned}
 \qquad\text{(14)}
\]
Absent negative-index terms are zero. Every supported degree-\(M\)
monomial has a positive coefficient. The central-cut factorization
contains the coefficientwise positive summand
\[
 (-1)^dH_C(x,b,c,y;-2)
       \ \ge_{\mathrm{coef}}\
          4(x+y)R_M(x,b,y)R_M(x,c,y).
 \qquad\text{(15)}
\]
The factor \(x+y\) has degree one and must be retained before the
shared extraction.

For odd \(N=2m+1\), there is a single zero diagonal, at row \(m\).
At \(-2\), a surviving path must visit this row. Splitting there and
reflecting the upper half proves the exact identity
\[
 H_C(x,b,c,y;-2)
       =R_m(x,b,y)R_m(x,c,y)
       =N^2D_m(x,b,y)D_m(x,c,y),
 \qquad\text{(16)}
\]
where \(R_m\) uses (14), and \(D_m=R_m/N\) is monic in its middle
variable. Indeed
\(\prod_{r=0}^{m-1}a_r=N\), by the noncentral sine product.
Paths skipping row \(m\) have an unused zero factor and vanish.
There is no forced outer unit at odd levels. Equation (16) is the
raw value of the full numerator, not its regularized spectral
derivative.

The local closed coefficient theorem gives the absolute rates
\[
 \begin{aligned}
 \frac1N\log[\boldsymbol L^{k_N}]R_{m-1}
      &\longrightarrow\sum_{f\in I}f(\alpha_f)
       &&(N=2m,\ |k_N|=m-1,\ k_N/N\to\alpha),\\
 \frac1N\log[\boldsymbol L^{k_N}]D_m
      &\longrightarrow\sum_{f\in I}f(\alpha_f)
       &&(N=2m+1,\ |k_N|=m,\ k_N/N\to\alpha),
 \qquad \sum_{f\in I}\alpha_f=\tfrac12 .
 \end{aligned}
 \qquad\text{(17)}
\]
The convergence holds uniformly on every closed supported triangle,
including singleton and two-corner faces. These are local statements:
the even normalization is proved in
[the half-block entropy theorem](actual_fejer_half_block_entropy.md),
§§4–5, and the odd shifted-mesh proof is in
[the odd numerator calculation](actual_fejer_odd_regularized_full_numerator.md),
§§2–3. The latter's later global flat-plat application is not used here.

The normalization in (17) is significant. At even levels the cleared
cofactor and the positive determinant at the neighboring maximum-fold
node differ only by polynomial factors, as the explicit product in the
half-block theorem shows. At odd levels \(R_m=ND_m\) exactly. The
local proofs use the original positive recurrence on a trimmed
interval, its coefficient estimate, and endpoint trimming and filling
with logarithmic cost
\(O(\varepsilon N\log(1/\varepsilon)+\log N)\).
Thus they apply to the bounded degree offsets below; no exponential
constant is absorbed into (17).

## 5. Rounding the table without changing a target

We first record the finite rounding argument used at both parities.
Suppose a supported nonnegative real table has integer row and column
sums. Subtract its entrywise floors. The remaining fractional table has
integer margins. In its bipartite row-column graph, alter entries
alternately around a cycle until an entry becomes zero or one, always
staying in \([0,1]\). This preserves all margins and reduces the
number of fractional entries. A nonempty forest of fractional entries
is impossible: a leaf would have an integer residual margin and exactly
one fractional entry. Repetition therefore produces an integer table
within the floor and ceiling of every original entry.

Before this rounding, a bounded correction to the column sums can be
made without changing row sums. Choose a spanning tree of the connected
ordinary spectator graph, and for each tree edge choose a spectator
triangle containing its two endpoints. Move the required column
imbalances along the tree, by subtracting at one corner and adding at
the other corner of that same row. A fixed bounded imbalance changes
every entry by a bounded amount. Since all \(\alpha_{tf}\) are positive
on the fixed support, the corrected tables below remain nonnegative
for all sufficiently large \(N\).

### Even levels

Let \(N=2m\), \(M=m-1\). Choose one ordinary outer face at each
spectator for the \(x+y\) factor in (15), and let \(c_f\) count these
choices. Such a face always exists: both outer endpoints cannot be
the protected pair, since their edge is matched and the protected
edge is unmatched in a simple sphere. In particular
\(\sum_f c_f=R-1\). Put
\[
 j_N=\lfloor M\lambda\rfloor,\qquad e_N=M\lambda-j_N\in[0,1).
 \qquad\text{(18)}
\]
Choose the cap monomial \(L_x^{j_N}L_z^{d-j_N}\). The two cofactor
rows per spectator must have row degree \(M\) and column totals
\[
 b_{f,N}=d-c_f-j_N\mathbf1_{f=x}
                    -(d-j_N)\mathbf1_{f=z}.
 \qquad\text{(19)}
\]
The initial table \(2M\alpha_{tf}\) has exact row sums \(M\).
Its required column correction is
\[
 \delta_f=
 \begin{cases}
  1-c_x+e_N,&f=x,\\
  -c_z-e_N,&f=z,\\
  1-c_f,&f\ne x,z .
 \end{cases}
 \qquad
 \sum_f\delta_f=0,\qquad
 \sum_f|\delta_f|<2R+2 .
 \qquad\text{(20)}
\]
Apply the tree correction and the rounding argument. The resulting
supported integer table satisfies
\[
 k_{tf,N}=2M\alpha_{tf}+O_D(1),\qquad
 \sum_f k_{tf,N}=M,\qquad
 \sum_t k_{tf,N}=b_{f,N}.
 \qquad\text{(21)}
\]
Aggregating each pair of triangle monomials with its chosen outer unit
gives one genuine central coefficient: each middle degree is at most
\(M\). The cap is left, since its overloaded middle degree is
\(d-j_N\ge m\). Equations (19)–(21) retain every original target.

### Odd levels

Let \(N=2m+1\), \(d=2m\), and put
\[
 j_N=\lfloor m\lambda\rfloor,\qquad e_N=m\lambda-j_N\in[0,1).
 \qquad\text{(22)}
\]
Since \(\lambda<1\), \(j_N\le m-1\), so this remains a genuine left
coefficient. There is no outer unit to choose. Each spectator row has
degree \(m\), with required column totals
\[
 b_{f,N}=d-j_N\mathbf1_{f=x}
                    -(d-j_N)\mathbf1_{f=z}.
 \qquad\text{(23)}
\]
Scale the original table by \(d=2m\). Equation (5) shows that its
column correction is just
\[
               \delta_f=e_N\mathbf1_{f=x}
                              -e_N\mathbf1_{f=z}.
 \qquad\text{(24)}
\]
It can be transported along one path from \(z\) to \(x\) in the
spectator graph, using only original row supports. Rounding gives
\[
 k_{tf,N}=d\alpha_{tf}+O_D(1),\qquad
 \sum_f k_{tf,N}=m,\qquad
 \sum_t k_{tf,N}=b_{f,N}.
 \qquad\text{(25)}
\]
Both spectator middle degrees are at most \(m\), as required for the
odd central piece. The cap's overloaded degree is at least \(m+1\).
Thus (25) is an actual array in the same original sector.

In either case \(k_{tf,N}/N\to\alpha_{tf}\). Positivity and the
factorizations (15)–(16) show that the contribution of the constructed
array is at least
\[
 \begin{cases}
 N\,4^{R-1}\displaystyle\prod_t
          [\boldsymbol L^{k_{t,N}}]R_{m-1,t},
                   &N=2m,\\[2mm]
 N^{\,2R-1}\displaystyle\prod_t
          [\boldsymbol L^{k_{t,N}}]D_{m,t},
                   &N=2m+1.
 \end{cases}
 \qquad\text{(26)}
\]
The factor \(N\) comes from (13). Applying (17) to the fixed finite
set of rows proves (8) on each parity, hence on the full sequence.

## 6. The unchanged 54-region diagram

Use the sphere, matching and original mark recorded in
[the singleton-sector certificate](actual_singleton_sector_envelope_obstruction.md),
§§2–5. It has \(56\) white vertices, \(162\) edges, \(108\) triangles
and \(54\) matched crossing regions. Its protected faces are \(29,50\),
and the selected ordered quartet is
\[
       e_*=32,\qquad (x,b,z,y)=(0,50,16,29),\qquad
       \lambda=\frac{548219162717}{10^{12}}.
 \qquad\text{(27)}
\]
The [exact certificate](../experiments/actual_singleton_sector_obstruction_certificate.json)
records all \(106\) spectator rows with their original face labels.
They satisfy (5) exactly, their ordinary support graph is connected,
and their minimum supported corner load is
\[
                   \frac{29141577}{40000000000}>0.
 \qquad\text{(28)}
\]
The same certificate verifies an original knot-producing parity
pattern. No terminal tangles or replacement diagram are involved.

Let \(Y_D\) be the actual complete augmented-link exterior supplied by
these marked sphere data, and write
\[
                       \Phi=\frac{\operatorname{Vol}(Y_D)}{2\pi}.
 \qquad\text{(29)}
\]
The complete action and this absolute volume normalization are
identified by [the original Morse geometry](actual_morse_geometric_contribution.md).
The rational interval certificate evaluates the entropy of the
feasible table from below, and the complete positive action at one
trial radius vector from above. It proves
\[
 E_{\mathrm{tab}}>67.8938190642,\qquad
 \Phi<67.6882466366,\qquad
                  E_{\mathrm{tab}}-\Phi>\frac15.
 \qquad\text{(30)}
\]
The second number is an upper bound for \(\Phi\), obtained by testing
its minimizing action; it is not an assertion that the trial radii are
the complete critical point. The
[rational verifier](../experiments/verify_actual_singleton_sector_obstruction.py)
uses exact target equations and outward interval bounds, with no
optimization in the verification.

Combining (8) and (30), at the one fixed tuple (7),
\[
 \boxed{\displaystyle
 \liminf_{N\to\infty}\frac1N
    \log\mathcal A_{N,\boldsymbol s}(+2,-2,\ldots,-2)
       \ge E_{\mathrm{tab}}>\Phi+\frac15 .}
 \qquad\text{(31)}
\]
The \(+2\) entry in this notation is region \(32\). This is a lower
bound for actual absolute local-coefficient products, not only for a
convex envelope or its dual relaxation.

## 7. Every positive diagonal Cauchy reference has the same limitation

For any finite complex array \((A_a)_{a\in I}\),
\[
 \inf_{w_a>0}
       \left(\sum_a w_a\right)^{1/2}
       \left(\sum_a\frac{|A_a|^2}{w_a}\right)^{1/2}
                  =\sum_a|A_a|.
 \qquad\text{(32)}
\]
Cauchy's inequality gives the lower bound. If no entry is zero, equality
holds for \(w_a=|A_a|\). Assign a positive weight tending to zero to
each zero entry to obtain the same infimum in general. If all entries
vanish, both sides are zero.

Apply (32) to the original array partition in (3). Even if the positive
reference may depend on the level, every spectrum, the full diagram and
the entire shared array, its best bound is exactly
\(\mathcal A_{N,\boldsymbol s}\). Equation (31) therefore rules out a
universal upper rate \(\Phi\) by this method. A shared positive face
gauge cannot change the conclusion: it multiplies every feasible array
by the same original target monomial, canceled by the coefficient
normalization. This also holds for level-dependent gauges.

This limitation concerns diagonal positive references on the unchanged
array partition. A non-diagonal Hermitian form or a regrouped sum can
retain phase correlations before taking absolute values. Equation (32)
does not rule out those estimates.

## 8. Exponential cancellation on the same odd levels

Let \(B_{N,j}\ge0\) be the original shared coefficient of the product
of positive central spectator polynomials, with targets \(d-j\) at
\(x\), \(j\) at \(z\), and \(d\) at every other ordinary face.
The protected variables remain zero. The finite identities are
\[
 \begin{aligned}
 S_{N,\boldsymbol s}(+2,-2,\ldots,-2)
       &=(-1)^{d(R-1)}
              \sum_{j=0}^{M}(-1)^jU_{N,j}B_{N,j},\\
 \mathcal A_{N,\boldsymbol s}(+2,-2,\ldots,-2)
       &=\sum_{j=0}^{M}U_{N,j}B_{N,j}.
 \end{aligned}
 \qquad\text{(33)}
\]
The two lines use the same exterior and the same targets.

For the diagram in §6, the separate
[uniform protected-interval theorem](research_cap_uniform_spectral_gap.md),
§§3–4, proves
\[
 \limsup_{\substack{N\to\infty\\N\ {\mathrm{odd}}}}
      \frac1N\log\sup_{\sigma\in[-2,2]}
       |S_{N,\boldsymbol s}(\sigma,-2,\ldots,-2)|
        \le\Phi-\eta,\qquad
 \eta=\min\{3/1000,\gamma_D\}>0.
 \qquad\text{(34)}
\]
Here \(\gamma_D\) is the strict omitted-tail capacity gap for the same
original exterior. Its hypotheses retain the actual odd factors
\(N^2D_mD_m\), their positive binary exterior after the other original
targets are extracted, the original cutoff \(M=m-1\), and the
certified untilted and tilted exterior pressures. In that theorem the
binary variables are \(A=L_{16}\), \(C=L_0\); therefore its protected
quartet \((C,0,A,0)\) and its coefficients \(p_j=B_{N,j}\) agree
literally with (27) and (33).

Take \(\sigma=+2\) in (34) and use the odd subsequence of (31).
With \(\log0=-\infty\),
\[
 \boxed{\displaystyle
 \limsup_{\substack{N\to\infty\\N\ {\mathrm{odd}}}}\frac1N
  \log\frac{|S_{N,\boldsymbol s}(+2,-2,\ldots,-2)|}
                {\mathcal A_{N,\boldsymbol s}(+2,-2,\ldots,-2)}
   \le-\bigl(E_{\mathrm{tab}}-\Phi+\eta\bigr)
   <-\frac15-\eta .}
 \qquad\text{(35)}
\]
The denominator is positive for every sufficiently large level by the
constructed arrays. Equation (35) is cancellation on the same odd
levels and at the same fixed tuple, rather than a comparison of
different parity subsequences.

No even-level signed gap is asserted here. Nor does (35) estimate the
other noncentral strings, simultaneous spectral variation at the
spectators, or the filling functionals. The conclusion is a precise
limitation of absolute summation and a precise instance of coherent
cancellation in the original finite source; it is compatible with an
eventual full knot-volume theorem.

## 9. Retaining the same flow does not repair the scalar energy score

There is a related obstruction to the refined coefficient score in
[the endpoint-conditioned energy criterion](general_endpoint_conditioned_source_energy.md),
§§5–6. We recall its definitions to distinguish this statement from a
bound for the signed sum.

The positive local reference is \(-V_N(-2)\) at even levels and
\(V_N(-2)-N^{-2}\partial_\sigma V_N(-2)\) at odd levels.
For a normalized incidence load \(\zeta=v/d\), let \(h(\zeta)\) be
the reference coefficient entropy. Let \(g(\zeta)\) be the proved
upper rate for the squared absolute coefficient divided by its positive
reference. The one-sided upper rate
\(h_{\mathrm{env}}(\zeta)\) is the perspective of the retained triangle
entropy. The combined score uses
\[
 h_{\mathrm{sharp}}(\zeta)
       =\min\{h_{\mathrm{env}}(\zeta),(h(\zeta)+g(\zeta))/2\}
                  \quad\text{on a one-sided load},
 \qquad h_{\mathrm{sharp}}=h_C\quad\text{on a central load}.
 \qquad\text{(36)}
\]
Here \(h_C\) is the largest sum of the two triangle entropies over
outer allocations giving that central four-incidence load.

On the protected left ray, the exact local formulas are
\[
 \begin{gathered}
 \zeta(u)=(u,0,1-u,0),\qquad 0\le u\le1/2,\\
 h(\zeta(u))=-2f(u),\qquad
 g(\zeta(u))=f(u)+f(1/2-u)=2f(u),\\
 h_{\mathrm{env}}(\zeta(u))=h_{\mathrm{sharp}}(\zeta(u))=0 .
 \end{gathered}
 \qquad\text{(37)}
\]
The reference and relative-energy identities are the protected case
of [the exact coefficient energy](actual_protected_outer_spectral_energy.md),
§2, and
[the one-sided triangle bound](actual_one_sided_relative_spectral_energy.md).
The perspective has mass \(2u\) and a singleton normalized row
\((1/2,0,0)\), whose entropy is zero. The value at \(u=0\) follows
by continuity. In particular, the vanishing score is not merely the
result of replacing a coefficient by a coarse, positive-radius bound.

Keep the table (5) and set \(u=\lambda/2\). At a spectator, aggregate
its rows \(\alpha=(\alpha_x,\alpha_b,\alpha_y)\) and
\(\beta=(\beta_x,\beta_c,\beta_y)\) to
\[
      \zeta_e=(\alpha_x+\beta_x,\alpha_b,\beta_c,
                                      \alpha_y+\beta_y).
 \qquad\text{(38)}
\]
Both middles are at most \(1/2\). The two original rows are a permitted
outer split, so \(h_C(\zeta_e)\) is at least their combined entropy.
Equations (5) retain all ordinary and protected face totals after this
aggregation. On central loads \(h=g=h_C\). Therefore the same single
feasible flow in the 54-region example satisfies
\[
 \sum_e h_{\mathrm{sharp}}(\zeta_e)\ge E_{\mathrm{tab}}>\Phi+\frac15,
 \qquad
 \sum_e(h(\zeta_e)+g(\zeta_e))
              \ge2E_{\mathrm{tab}}>2\Phi+\frac25 .
 \qquad\text{(39)}
\]
Thus neither universal scalar score inequality holds on arbitrary
matched simple-sphere Morse diagrams at their prescribed mark. This
does not contradict the conditional implications of the energy
criterion. That note asks its universal question on the narrower
class of certified flat plats; the present construction does not
identify this marked sphere with a member of that class.

Strict concavity of complete triangle entropy does not compare these
two different feasible sets. In the complete problem the missing
input triangle of (4) puts load \(1/2\) on \(x\). If its output
triangle puts load \(r\) on \(x\), the restored totals of the fixed
spectator table would be
\[
     1+(1/2-u+r)\quad\text{at }x,\qquad
     1-(1/2-u+r)\quad\text{at }z .
 \qquad\text{(40)}
\]
Since \(u<1/2\) and \(r\ge0\), these fail the complete face equations.
The feasible noncentral table is consequently not a complete angle
structure with the same faces. No nonhyperbolic representation or
cone metric is inferred from it; the exact signed cancellation is
instead the statement proved in (35).

## 10. Finite verification and proof scope

The [source checker](../repro/check_absolute_source_obstruction.py)
independently evaluates the original polynomial matrix
\(V_N(\sigma)\) over finite fields, checks its protected coefficients
and odd central factorization, and constructs exact rounded tables
with the original targets. Those are finite checks of the identities
and incidences. The all-level lower bound uses the written rounding
argument and the uniform local coefficient theorem (17), not an
extrapolation from the checked levels.

The complete-volume comparison (30) uses the separate marked
geometric construction and its rational action certificate. The
signed upper bound (34) uses the separate stable-exterior theorem,
its pressure certificates and omitted-tail gap. These inputs have
different purposes; none follows merely from the finite-field
checks or the absolute-array construction.
