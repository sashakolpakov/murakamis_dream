# Full internal labels at a two-junction component, and a coupled clamping question

Private derivation, 1 November 2026. No repository source is changed.

The present component theorem cuts every retained edge at one half. That cutoff cannot be kept for arbitrary bare components: a genuine two-junction component already has its complete maximum on the cutoff. Keeping that internal label gives an exact Gram identity and a source theorem for this smallest adjacent component, with no boundary-count hypothesis. The last sections isolate a possible general comparison and an exact obstruction to its coordinatewise version.

## 1. Exact conventions and the comparison inputs

Use the fixed complete basis and physical relations from `notes/actual_main_meridian_source_bounds.md`:
\[
 d=N-1,\quad M_N=\lfloor d/2\rfloor,\quad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad
 e_j(z)=S_j^{-2}\prod_{r=0}^{j-1}(c_r-z),
 \quad c_r=2\cos((2r+1)\pi/N).
 \tag{1}
\]
Write \(P_\sigma=\mathsf T_N+2\cos(2\pi\sigma)\), where the actual type chooses \(\sigma=0,s\), or \(-s\). The normalized trace and unchanged metric are
\[
 \phi_\sigma(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_\sigma}F,
 \qquad \phi_\sigma(e_i e_j)=\mathbf1_{i+j=d}.
 \tag{2}
\]
Every actual physical turn edge in lower-index convention has tensor
\[
 D_r(s)=\gamma_N(s)\frac{H_N(s)}{W_r(s)},\qquad
 W_r(s)W_{d-r}(s)=H_N(s)^2.
 \tag{3}
\]
Its two incident indices are equal. The prescribed scalar \(\gamma_N\) is kept. For every fixed \(|s|\le R<1\), both \(D_r\) and its inverse are bounded uniformly in \(N,r\). These facts concern a physical turn edge; an artificial unturned edge introduced by resolving a larger product instead identifies complementary labels.

Let \(J(u)=\int_0^u\log(2\sin\pi t)\,dt\), \(g(u)=J(2u)-4J(u)\) on \([0,1/2]\), and \(G_0=g(1/4)=2G/\pi\), with \(G\) Catalan's constant. Four boundary arrays satisfy
\[
 F_{a,N,s}=\sum_{j=0}^d f_{a,N,s,j}e_j,\qquad
 |f_{a,N,s,j}|\le e^{N(c_a+o(1))}
 \begin{cases}e^{Ng(j/N)},&j\le M_N,\\1,&j>M_N.
 \end{cases}
 \tag{4}
\]
The errors are uniform over the actual physical input parameters and the chosen main disk. The constants are fixed. The arrays may be complex and need not attain these bounds.

An output norm is included by using as the fourth boundary array the positive probe
\[
 W_N^{\mathrm{probe}}=\sum_{j\le M_N}e_j(-2)e_j+\sum_{j>M_N}e_j.
 \tag{5}
\]
Its coefficient rate is exactly (4) with \(c_4=0\), up to \(O(\log N)\). The full value-and-first-normal norm obeys
\(\|e_j\|_{\mathcal J}\le N^C[e_j]W_N^{\mathrm{probe}}\).
When the output itself is a typed turn, its exact extractor adds the factor \(\gamma_NH_N/W_j\) to the probe coefficient. It is retained in the finite expression and costs only the uniform constant from (3) in the norm bound. This probe only bounds the output; it is not inserted into the knot.

## 2. The two-junction Gram identity

Consider two trivalent bare vertices joined by one physical turn. Each has two boundary factors. If all four factors are supported on low indices, their ordinary products
\[
 A=F_1F_2=\sum_{k=0}^d A_k e_k,\qquad
 B=F_3F_4=\sum_{k=0}^d B_k e_k.
 \tag{6}
\]
have degree at most \(2M_N\le d\). Thus no quotient reduction occurs in either product, regardless of which vertex relation is moving. Their complete positive multiplication table determines the coefficients in (6).

The covariant trace at the first vertex equals \(A_{d-r}\), by (2); the second equals \(B_{d-r}\). Consequently the whole component is exactly
\[
 \boxed{\quad
 \mathcal C_s(F_1,F_2,F_3,F_4)
 =\sum_{r=0}^dD_r(s)A_{d-r}B_{d-r}
 =\frac{\gamma_N(s)}{H_N(s)}
                 \sum_{k=0}^d W_k(s)A_kB_k.
 \quad}
 \tag{7}
\]
This is an identity with all canonical coefficients and all normals retained. In particular its internal index is not restricted to the low range.

For nonnegative arrays the same expression at completeness is a positive Gram contraction. For arbitrary complex low arrays, replace each boundary coefficient by its modulus before forming \(A^{\mathrm{abs}},B^{\mathrm{abs}}\). Complete Newton multiplication is positive, hence
\[
 |\mathcal C_s(F_1,F_2,F_3,F_4)|
 \le C_R\sum_k A_k^{\mathrm{abs}}B_k^{\mathrm{abs}}.
 \tag{8}
\]
The same assertion holds for an arbitrary prescribed set of internal indices. It is a coefficientwise positive majorant of the full internal sum, not an operator-norm comparison of a general turn.

## 3. The coupled complete pressure

Let
\[
 h_N=\sum_{j\le M_N}a_{N,j}e_j,
 \qquad a_{N,j}=\frac{N^2S_{2j}}{S_j^4},\qquad
 h_N^2=\sum_k A_{N,k}^0e_k.
 \tag{9}
\]
The closed low coefficient rate of \(h_N\) is \(g\). Write \(f_2(x)\) for the actual positive coefficient profile of \(h_N^2\). It is the constrained maximum of
\(g(u)+g(v)+m(u,v,x)\) on the original gate domain. The original two-leaf stationarity gives
\[
 f_2'(x)=2\log(2X^2),\qquad
 X=\frac{\cot\pi x+\sqrt{\cot^2\pi x+2}}2.
 \tag{10}
\]
Thus the unique maximum is at \(x=1/2\). Positivity, the uniform closed sine-factorial rates, and strict integer approximation at this output give at both parities
\[
 \Phi_{\mathrm{pair}}
 :=\lim\frac1N\log\sum_k(A_{N,k}^0)^2
 =2f_2(1/2).
 \tag{11}
\]
This is the original closed pressure of the two-junction tree with four effective pure leaves. Its derivation keeps the common internal label; it does not sum independent cap pressures.

A useful exact lower bound needs no solution of the stationary equations. The feasible state \(u=v=1/4,x=1/2\) has
\[
 m(1/4,1/4,1/2)=G_0,
 \qquad f_2(1/2)\ge3G_0,
 \qquad \Phi_{\mathrm{pair}}\ge6G_0.
 \tag{12}
\]
The state lies on one gate face, which is allowed for this lower bound. Finite indices with \(u=v=\lfloor N/4\rfloor/N\) and \(k=2\lfloor N/4\rfloor\) give the same limiting rate. The actual maximizer used for (11) is strict.

The full component action is
\[
                         \Omega=\sum_{a=1}^4c_a+\Phi_{\mathrm{pair}}.
 \tag{13}
\]
The constants are affine because each boundary array occurs once. If the fourth array is the probe, set its constant to zero.

Equation (8), the polynomial comparison of low coefficient envelopes with (9), and (11) prove the action bound \(e^{N(\Omega+o(1))}\) for the all-low boundary sector. Internal labels above one half remain inside this leading comparison.

## 4. High boundary sectors and genuine return terms

The exact covariant cubic tensor is the sum of the old positive tensor and the return tensor. The old support is
\[
 i+j,\ i+k,\ j+k\le d,\qquad i+j+k\ge d.
 \tag{14}
\]
Its logarithmic action is
\[
 t(x,y,z)=J(x+y)+J(x+z)+J(y+z)
          -J(x)-J(y)-J(z)-J(x+y+z-1).
 \tag{15}
\]
It equals the old product action after setting its output to \(1-z\). The decomposition into three ideal tetrahedron volumes gives
\[
                              t\le\frac{3v_3}{\pi}.
 \tag{16}
\]
This is the decomposition in `notes/actual_conway_general_core_packet_and_gap.md`, Section 3, including boundary states.

The return support is
\[
 i+j,\ i+k,\ j+k\ge N,\qquad i+j+k\ge2N-1.
 \tag{17}
\]
Its absolute coefficient is \(|\Delta_\sigma|\Lambda(i,j,k)\), with
\[
 \Delta_\sigma=2\cos(2\pi\sigma)-2,\quad
 t_0=i+j+k-(2N-1),\qquad
 \Lambda(i,j,k)=
 \frac{N^2}{S_iS_jS_kS_{t_0}S_{i-t_0}S_{j-t_0}S_{k-t_0}}.
 \tag{18}
\]
The complete alternating sign remains in the actual tensor. For the estimate in this section only, we take its absolute value. The exact quotient proof in `/private/tmp/md-fixed-newton-return-gates-and-contracted-tensor.md` gives a uniform polynomial bound for \(\Lambda\). Its uniform closed rate, with \(a=1-i/N,b=1-j/N,c=1-k/N\), is
\[
 \mathcal R(a,b,c)=J(a)+J(b)+J(c)+J(a+b+c)
          -J(a+b)-J(a+c)-J(b+c)\le0,
 \tag{19}
\]
where \(a,b,c\ge0,a+b+c\le1\). The full-region proof is
\[
 \mathcal R(a,b,c)
 =-\pi^2\int_0^a\int_0^b\int_0^c
        \csc^2(\pi(u+v+w))\,dw\,dv\,du.
 \tag{20}
\]
Its corner singularities are integrable. The inequality is strict if all three complements are positive, even on their total-one face.

Every return vertex has at least two high incidences, since two low indices have sum at most \(d<N\). At a vertex of this two-junction component, at most one incidence is internal. Therefore a return requires at least one high external boundary input. This statement includes a high output probe.

Expand the two tensors into their old and return parts. If neither is a return, the complete positive sector with any high boundary has the strict gap supplied by `notes/actual_conway_unflagged_core_probe_bound.md`, Sections 2–4. Its proof applies to arbitrary low \(g+c\)/high \(c\) arrays, not only physical alias arrays. Bounded paired edge weights preserve that positive majorant.

If exactly one vertex is a return, at least one of the four boundary indices is high. The boundary rates add to at most \(\sum c_a+3G_0\). Equations (16),(19) give the total rate at most
\[
                         \sum c_a+3G_0+\frac{3v_3}{\pi}.
 \tag{21}
\]
If both vertices are returns, at least two boundary indices are high, and the rate is at most \(\sum c_a+2G_0\). In an actual typed edge the two-return case is absent, as Section 6 explains, but this estimate does not need its absence.

The elementary bounds recorded in the isolated three-leaf proof give
\[
 v_3<\frac{273}{256},\qquad
 4G>\frac{32}{9},\qquad 3v_3<4G.
 \tag{22}
\]
Therefore \(3v_3/\pi<2G_0\). Comparing (21) and the two-return bound with (12) shows that every new return sector has a loss strictly greater than \(G_0\) from \(\Omega\). Uniform factorial errors and the fixed polynomial number of states preserve any smaller positive loss. This includes all endpoint return states and all \(|s|\le R<1\); zeros of \(\Delta_\sigma\) only improve the upper bound.

We have proved a full component theorem: the norm is bounded at the original action (13), and every sector with a high boundary input or a high output probe has a strict exponential gap. Its clean term keeps every boundary input and its output low, but sums the entire internal label. If an inherited error lowers one whole boundary coefficient cone by \(\eta\), affine homogeneity in (13) preserves that deficit. Thus this component may replace a singleton or a path-qualified component in the existing flagged/bare mutual source induction. It admits arbitrary repeated occurrences separated by flagged junctions; no independent cap budget is added.

## 5. Why the internal half cutoff fails, and the correct local window

The positive complete internal law in (11) has its maximum at \(k/N=1/2\). Its covariant edge label is \(r=d-k\), so it too tends to one half. Choose supported indices with \(r>M_N\) and \(r/N\to1/2\). Strict approximation of the two original pair fibers gives the same limiting action \(\Phi_{\mathrm{pair}}\) on these individual terms. Hence the complete internal-high sector has no fixed exponential deficit. This is an exact obstruction to extending the published all-retained-low invariant unchanged.

It causes no singularity in the actual local saddle. At every strict old cubic vertex, the three pair sums are less than one, so its total normalized degree is less than \(3/2\). On a fixed sufficiently small original maximizing window, the raw polynomial degree is therefore less than \(2N-1\). One division by \(P_0\) then has quotient degree at most \(N-2\), and
\[
                      \phi_\sigma(e_i e_j e_k)=\phi_0(e_i e_j e_k)
 \tag{23}
\]
exactly on that window, even if one of its indices is above \(M_N\).

Only circle-incident labels must stay in a compact low interval for the circle trace and angular Gaussian. The internal bare–bare label may cross one half while remaining in a compact subset of \((0,1)\). Its exact edge interpolation and bulk expansion remain regular there:
\[
 \frac{H_N(s)}{W_{Nx}(s)}
 =\frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}
 =1-\frac{\pi s^2}{N}\cot(\pi x)+O_R(N^{-2}).
 \tag{24}
\]
The first equality at nonintegral \(Nx\) defines the canonical interpolation. Original strict gate arguments stay positive at this half-label state. Thus the finite primitive window and strict Hessian can be treated by the same grouped contour construction, retaining this full internal coordinate. This paragraph identifies the local interface; it does not assert an independently assembled filled theorem for the enlarged class.

## 6. Actual typing isolates moving return vertices

The six-type physical turn table has the four-cycle
\[
 \operatorname{End}(++)\longrightarrow
 \operatorname{Hom}(-+,+-)\longrightarrow
 \operatorname{End}(--)\longrightarrow
 \operatorname{Hom}(+-,-+)\longrightarrow
 \operatorname{End}(++),
 \tag{25}
\]
and interchanges the two opposite-color endomorphism spaces. Only the equal-color endomorphism spaces have the moving relation; all four opposite-order spaces have the constant relation. At a lowered product vertex, compatibility makes its factors share that Casimir class. Hence every original physical turn edge has at least one constant-relation endpoint: moving vertices form an independent set.

This applies to the original reduced junction tree, not to unturned edges introduced in an artificial binary resolution of a high-valence product. In a trivalent physical-turn tree, distinct return vertices therefore cannot be adjacent. Their high incidences end in old vertices, which have at most one high incidence each. This is a useful extra restriction on the return sectors. It does not by itself control the pressures of the old regions joining several return vertices.

## 7. A coupled pressure obstruction and the remaining general lemma

For a general trivalent component, remove its return vertices and consider one connected remaining old region. Its boundary can have several prescribed high labels \(z_1,\ldots,z_r\). Let \(\Psi(z_1,\ldots,z_r)\) be its actual old constrained pressure, including every ordinary leaf profile and constant. A sufficient simultaneous-clamping statement would be
\[
 \Psi(z_1,\ldots,z_r)\le\Psi(1/2,\ldots,1/2)
                  \quad(z_j\ge1/2).
 \tag{26}
\]
If (26) held, all regions could be reoptimized simultaneously at the half interfaces, without adding independent caps. Each return vertex would be replaced by an old vertex with two or three half incidences; its old action is nonnegative whereas its return action is nonpositive. The resulting feasible old state has a saturated pair-sum inequality. The original strict maximum then gives a uniform positive boundary gap. This is only a conditional global argument: (26) has not been established here.

The tempting coordinatewise strengthening of (26) is false even for a genuine positive old region. Take two old trivalent vertices joined by label \(u\), each with one physical pure leaf, and prescribe the remaining boundary labels \(z,w\). Its coupled pressure is
\[
 \Psi(z,w)=\max_{a,b,u}
   \{g(a)+g(b)+t(z,a,u)+t(w,b,u)\},
 \quad a,b\in[0,1/2],
 \tag{27}
\]
with the two original old support domains. At \(w=1\), the second vertex forces \(b=u=0\). The first forces \(a=1-z\), and both cubic actions are zero. Thus
\[
                    \Psi(z,1)=g(1-z),\qquad
 \Psi(3/4,1)=G_0>0=\Psi(1/2,1).
 \tag{28}
\]
This also gives an interior failure. Put \(w=1-\epsilon\), \(u=b=3\epsilon/4\), and \(a=1-z-3\epsilon/8\). For \(z=1/2\) or \(3/4\), all old gate inequalities and both leaf ranges are strict for sufficiently small \(\epsilon>0\), and the action tends to \(g(1-z)\). Compactness gives the matching upper limit, since every limiting feasible state at \(w=1\) is the forced state above. Consequently \(\Psi(3/4,w)>\Psi(1/2,w)\) for all sufficiently large \(w<1\).

Thus the derivative bound for a one-output complete branch cannot be applied one coordinate at a time to a region with several prescribed interfaces. The simultaneous inequality (26) is not contradicted by (28), because it also changes \(w\). Since the old joint pressure is concave, one possible proof of (26) would be a nonpositive supporting gradient at the all-half boundary. Strict angle feasibility at the all-half assignment is elementary here: each old vertex has at most one marked high-boundary incidence. Set those incidences to \(1/2\), and all other internal and ordinary-leaf labels to \(3/8\). An unmarked cubic has total \(9/8\) and pair sums \(3/4\); a marked one has total \(5/4\) and largest pair sum \(7/8\). Both are strict. What is not yet proved is that the constrained maximizer is strict and supplies positive boundary multipliers. Establishing those properties and the supporting gradient is a new geometric obligation; they do not follow solely from this feasible angle assignment or from the existing one-output probe theorem.

For higher-valence bare vertices, even the trivalent physical-edge support reduction needs further work: a raw low product can have a nonzero return trace without a high exterior label. The regular low-window Fourier comparison remains available, but it is not a global high-sector theorem. No general arbitrary-component moving-meridian bound or volume equality is claimed here.
