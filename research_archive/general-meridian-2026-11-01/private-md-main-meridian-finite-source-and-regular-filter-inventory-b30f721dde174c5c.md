# The main-meridian cut source and its canonical regularization

Private continuation, 31 October 2026. No repository or release file is changed.

## 1. What the strict Conway estimates do and do not vary

The strict-tree source theorem does not presently give an analytic family in the main unrolled color. In `actual_odd_conway_complex_color_packet.md`, Section 1, its variables are the auxiliary-circle deficits \(t_i=h_i/N\), and its physical leaves are \(T(R^{\epsilon_i}L_{N-h_i})\). The main strands still carry the fixed module \(V_{N-1}\). The larger scope of `actual_conway_general_core_packet_and_gap.md` changes the allowed tree and includes quarter-index states; it does not change that main module. The coefficient-cone theorem in `actual_conway_unflagged_core_probe_bound.md` still uses the complete quotient, its repeated nodes, the basis reversal \(Te_r=e_{N-1-r}\), and the complete marked pairing.

There is a geometric check of the distinction: `actual_conway_general_mask_marked_filling.md`, Section 5, computes the two adjacent white transitions and proves that the main-meridian multiplier remains identically one throughout its auxiliary deformation. It is a parabolic main cusp throughout. The auxiliary filling equations and their complex packet consequently do not provide a main-meridian saddle by changing the name of a parameter. The pointed quantum-A note states the same limitation explicitly near its end.

There is, however, an exact finite source for the main-meridian family, and its regular remainder can also be written as an exact finite source. Sections 2–5 give formulas with their full normalization. Their analytic limitations are stated in Section 7.

## 2. The literal cut state at \(\alpha=N-1+s\)

Fix a zero-framed knot braid with \(b\) strands, \(L\) crossings and writhe \(w\). Put

\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \alpha=d+s,\quad x=q^{d+s}=-q^{s-1},\quad
 M=-qx=q^s,\quad Y=M^2=Q^s,\quad \kappa_D=w-b+1.
\tag{1}
\]

All powers use this displayed exponential, including for complex \(s\). The actual color has

\[
 H v_a=(d+s-2a)v_a,\quad K v_a=xq^{-2a}v_a,
 \quad E v_a=[a]_q[d+s-a+1]_qv_{a-1},\quad Fv_a=v_{a+1},
\tag{2}
\]

with indices \(0\le a<N\) and zero endpoint vectors. At fixed root these are the actual unrolled matrices. For a positive checked crossing the output is \((b_0+k,a-k)\), with \(0\le k\le\min(a,d-b_0)\); for a negative crossing it is \((b_0-k,a+k)\), with \(0\le k\le\min(b_0,d-a)\). Using \(b_0\) for the local second head to avoid confusion with the braid width, the stripped coefficients are exactly

\[
\begin{aligned}
 r^+_s(a,b_0,k)
 &=(-1)^k x^{-a-b_0-k}
   Q^{ab_0+(a-b_0)k-k(k+1)/2}
   {a\brack k}_Q(Q^{s-a};Q)_k,\\
 r^-_s(a,b_0,k)
 &=x^{a+b_0-k}Q^{-ab_0}
   {b_0\brack k}_Q(Q^{s-b_0};Q)_k.
\end{aligned}
\tag{3}
\]

These are the literal highest-weight-basis formulas in `relative_octahedral_period.md`, Section 1. Other notes use a common-Verma basis with different Gaussian indices. No such basis is substituted in (3).

The common Cartan scalars cancel against the zero-framing twist exactly as in `kashaev_ado_pointing.md`, Section 1. The remaining framing line is \(x^{wd}\), and every traced strand retains \(K^{-d}\). The reduced knot family is the \((0,0)\) entry of this cut partial trace. Its value at \(s=0\) is the reduced Kashaev invariant \(K_N\), not the full modified invariant. The latter still has

\[
 \mathcal N_N(M)=\eta_N\frac{M^{N-1}}{S_N(M^2)}F_N(M),
 \qquad S_N(Y)=1+Y+\cdots+Y^{N-1},\quad \eta_N=i^{N+3}.
\tag{4}
\]

No factor of (4) is erased when passing to a meridian germ.

Every admissible crossing weight at \(s=0\) is nonzero: each Pochhammer uses only \(1-Q^{-m}\) with \(1\le m<N\), and its Gaussian denominator has indices below \(N\). Thus a complete cut path \(\sigma\) has a well-defined entire relative insertion

\[
\begin{aligned}
 \frac{r^+_s}{r^+_0}
 &=q^{-s(a+b_0+k)}
     \prod_{m=a-k+1}^{a}\frac{1-Q^{s-m}}{1-Q^{-m}},\\
 \frac{r^-_s}{r^-_0}
 &=q^{s(a+b_0-k)}
     \prod_{m=b_0-k+1}^{b_0}\frac{1-Q^{s-m}}{1-Q^{-m}},\\
 \frac{W_\sigma(s)}{W_\sigma(0)}
 &=q^{sd\kappa_D}
   \prod_{\text{crossings}}\frac{r^{\mathrm{sign}}_s}
                                      {r^{\mathrm{sign}}_0}.
\end{aligned}
\tag{5}
\]

The last factor contains the changes of all closed pivots and the residual framing. Even knot parity does not permit setting it to one for nonintegral \(s\). Formula (5) is an identity before summing; it makes no assertion about a relative ratio of the contracted knot scalars.

## 3. A useful but strictly precontraction bound

On \(|s|\le R\), set \(A_R=\pi R e^{\pi R}/2\). For \(1\le m<N\),

\[
 \frac{|1-Q^{s-m}|}{|1-Q^{-m}|}
 \le 1+\frac{A_R}{\min(m,N-m)}.
\tag{6}
\]

Indeed \(|Q^s-1|\le2\pi R e^{\pi R}/N\), whereas
\(|1-Q^{-m}|\ge4\min(m,N-m)/N\). The harmonic sum over these denominators is at most \(2(1+\log N)\). Every Pochhammer quotient in (5) is consequently bounded by \(e^{2A_R}N^{2A_R}\). Its explicit q-power is bounded by a constant on this disk, since the head exponents have absolute value at most \(2d\). The fixed pivot/framing factor has modulus at most \(e^{\pi R|\kappa_D|}\). Therefore

\[
 \sup_{|s|\le R}|W_\sigma(s)|
       \le C_{D,R}N^{2LA_R}|W_\sigma(0)|
\tag{7}
\]

uniformly over all actual cut paths and both level parities. Cauchy's formula on a slightly larger disk gives polynomial bounds for every fixed derivative of the relative insertion as well. Zeros at integral shifted colors cause no problem, since only the nonzero complete denominator was divided.

This is not a polynomial comparison with \(|K_N|\). Summing (7) produces the absolute cut-state sum \(\sum_\sigma|W_\sigma(0)|\), whose exponential rate need not be the selected knot rate. The strict Conway proof controls a different, recoupled signed source with its own cancellation estimates. A transfer of (7) through that recoupling has not been established.

Also \(|s|\le R\) means \(|\log M|=O(1/N)\). It is not a fixed neighborhood of \(M=1\). The constants in (7) are not uniform for \(|s|\) proportional to \(N\).

## 4. A finite regularization filter, including negative exponents

Write the even meridian family as \(F_N(M)=f_N(Y)\). Its evenness is statewise in the finite cut sum: `even_meridian_norm_descent.md`, Section 2, proves that the total x-exponent

\[
 E_\sigma=d\kappa_D+
 \sum_+(-a-b_0-k)+\sum_-(a+b_0-k)
\tag{8}
\]

is even by the integer-position conservation law. Thus every path is a Laurent monomial in \(Y\), times finite Pochhammers in \(Y\), without first invoking cancellation between paths.

Let \(I_N\) be interpolation on the \(N-1\) nontrivial Nth roots, with values in polynomials of degree at most \(N-2\). The ordinary-color pointing gives \(I_N f_N=P_N^{\mathrm{ord}}\). Define the linear map

\[
 \mathcal D_Nf=\frac{f-I_Nf}{S_N}.
\tag{9}
\]

For any integer exponent write its Euclidean division as \(\ell=kN+t\), where \(k\in\mathbb Z\) and \(0\le t<N\), and put \(U=Y^N\). Then

\[
 \boxed{\quad
 \mathcal D_N(Y^\ell)
 =Y^t(Y-1)G_k(U)+\mathbf1_{t=N-1},\qquad
 G_k(U)=\frac{U^k-1}{U-1}.
 \quad}
\tag{10}
\]

Here \(G_k\) is a Laurent polynomial, with

\[
 G_k(U)=
 \begin{cases}
  \sum_{j=0}^{k-1}U^j,&k>0,\\
  0,&k=0,\\
  -\sum_{j=k}^{-1}U^j,&k<0.
 \end{cases}
\tag{11}
\]

To prove (10), the root values of \(Y^\ell\) equal those of \(Y^t\). If \(t\le N-2\), its interpolant is \(Y^t\). If \(t=N-1\), its interpolant is
\(Y^{N-1}-S_N=-\sum_{j=0}^{N-2}Y^j\), which has the required degree. Now use \(U-1=(Y-1)S_N\). This proves every case, with no division by a sampled zero.

For example \(\ell=-1\) has \(k=-1,t=N-1\), and (10) gives \(\mathcal D_N(Y^{-1})=Y^{-1}\). For \(\ell=-N\), it gives \(-Y^{-N}(Y-1)\). For \(\ell=N-1\), it gives exactly one. These examples verify both the negative-k sign and the exceptional interpolation row.

At completeness the filter reduces to

\[
 R_N^{\mathrm{reg}}(1)
 =\sum_{\ell\equiv N-1\ (\mathrm{mod}\ N)}[Y^\ell]f_N(Y)
 =\frac1N\sum_{j=0}^{N-1}Q^j f_N(Q^j).
\tag{12}
\]

The actual ordinary-color pointing further writes this as
\(R_N^{\mathrm{reg}}(1)=[K_N+\sum_{j=1}^{N-1}Q^jC_j(q)]/N\),
consistent with
\(P_N^{\mathrm{ord}}(1)=-\sum_{j=1}^{N-1}Q^jC_j(q)\).
These are exact signed extraction formulas, not estimates of their
individual coefficient contributions.

Equation (12) is already the cyclic-trace formula in `regularized_kashaev_period.md`, Section 5. It is not being presented as a new complete-point identity. I checked that note, `central_source_freedom_in_regular_profiles.md`, and `scaled_meridian_regular_profile.md`, including their division and central-multiplier formulas. They supply the canonical quotient, the complete trace and the whole-profile comparison; I did not find the explicit all-integer monomial rule (10) there. It is recorded as an elementary formula for the existing regularization, not as a new invariant or a novelty claim.

## 5. The regular remainder is an exact finite cut sum

Each path weight in Section 2 has the form

\[
 c_\sigma Y^{e_\sigma}
      \prod_{v=1}^{L}(YQ^{-a_v};Q)_{k_v},
\tag{13}
\]

where at a negative crossing \(a_v\) means its second incoming head. The coefficient \(c_\sigma\) contains all the Gaussian, phase, pivot and framing factors, and \(e_\sigma=E_\sigma/2\) is integral. The finite q-binomial identity expands one factor as

\[
 (YQ^{-a};Q)_k
 =\sum_{r=0}^{k}(-1)^rQ^{r(r-1)/2-ar}
                  {k\brack r}_QY^r.
\tag{14}
\]

There is one extra integer index per crossing, with its original bound \(0\le r\le k<N\). All factorial denominators remain root units. For the fixed braid the resulting number of states is polynomial in \(N\); no exponentially large binary expansion is necessary. Write the resulting exact Laurent expansion as a state sum

\[
 f_N(Y)=\sum_{\sigma,\mathbf r}c_{\sigma,\mathbf r}Y^{\ell_{\sigma,\mathbf r}}.
\]

The actual crossing support gives the bound term by term. A positive
crossing contributes M-exponent \(-a-b_0-k+2r\in[-2d,0]\): use
\(k\le a\) for its upper end and \(k\le d-b_0\) for its lower
end. A negative crossing contributes
\(a+b_0-k+2r\in[0,2d]\), using its two corresponding bounds.
Including the common exponent \(d\kappa_D\), every surviving even
M-exponent therefore gives
\[
 -\frac{d(L+b-1)}2\le\ell_{\sigma,\mathbf r}
             \le\frac{d(L-b+1)}2.
\tag{14a}
\]
Consequently the integer quotient \(k=\lfloor\ell/N\rfloor\) in
(10) ranges over a fixed finite set, independent of level. Linearity
of interpolation gives the pole-free exact source

\[
 R_N^{\mathrm{reg}}(Y)
 =\sum_{\sigma,\mathbf r}c_{\sigma,\mathbf r}
   \left[Y^{t_{\sigma,\mathbf r}}(Y-1)
                     G_{k_{\sigma,\mathbf r}}(Y^N)
          +\mathbf1_{t_{\sigma,\mathbf r}=N-1}\right].
\tag{15}
\]

No separately chosen ordinary-color data or singular termwise quotient is required to evaluate (15). Its equality with the canonical ordinary-color subtraction uses the proved pointing once, through \(I_Nf_N=P_N^{\mathrm{ord}}\). Every coefficient in (15) still comes from the literal cut source.

For \(Y=Q^s=e^{2\pi is/N}\), bounded complex \(s\), the global filter in square brackets satisfies

\[
 \mathcal D_N(Y^\ell)\big|_{Y=Q^s}
             =\mathbf1_{\ell\equiv N-1\ (\mathrm{mod}\ N)}
                    +O_{D,R}(N^{-1}),
\tag{16}
\]

uniformly in all its states, including \(t/N\in[0,1]\), negative k, and integer \(s\). This follows from \(U=e^{2\pi is}\), the bounded finite sums in (11), \(|Y^t|\le e^{2\pi R}\), and \(Y-1=O_R(1/N)\). In particular no difficulty occurs at \(U=1\).

One must not sum the error in (16) relative to \(K_N\) without a source estimate. Its immediate bound is
\(O_{D,R}(N^{-1})\sum_{\sigma,\mathbf r}|c_{\sigma,\mathbf r}|\),
not \(O(N^{-1})|K_N|\). The added q-binomial expansion and residue filter can expose cancellations not controlled by the complete Conway positive envelope. Formula (15) supplies exact algebraic access, not a saddle or a sharp absolute majorant.

## 6. Which uniformity is already available

The existing regular-period theorem bounds the ordinary interpolation coefficients by \(2D_N\), where \(D_N=O_K(N^{b-1})\). The strict/net-twist positive-volume theorem gives \(|K_N|=\exp(Nv+o(N))\), \(v>0\), for its knots. Thus the tail-domination assumption of `scaled_meridian_regular_profile.md` is satisfied on these proved classes.

Using that note's variable \(z=2\pi is\), define

\[
 g_N(z)=\frac{f_N(e^{z/N})}{K_N},\qquad
 \rho_N(z)=e^{(N-1)z/(2N)}
                \frac{N R_N^{\mathrm{reg}}(e^{z/N})}{K_N}.
\]

It already proves the exact identity

\[
 g_N=H_N\rho_N+\pi_N,\qquad
 H_N(z)=\frac{\sinh(z/2)}{N\sinh(z/(2N))},\qquad
 \pi_N(z)=\frac{P_N^{\mathrm{ord}}(e^{z/N})}{K_N},
\tag{17}
\]

where \(\pi_N\to0\) locally uniformly with every fixed derivative. On fixed compact sets \(H_N\to2\sinh(z/2)/z\), and exact divisibility plus a boundary maximum principle gives uniform division through all fixed resonances. Local boundedness, or local uniform convergence, of \(g_N\) is equivalent to the corresponding property of \(\rho_N\). Neither property is established there for the selected knot family.

Several related exact results must be kept distinct. `meridian_casimir_source.md` supplies the genuine moving local nodes
\(c_j(Y)=q^{-2j-1}Y+q^{2j+1}Y^{-1}\), the crossing values and their confluence. `actual_open_meridian_horizontal_source_transport.md` gives source-preserving gauges and a genuine insertion for a meridian shift, but explicitly does not bound the contracted insertion. `actual_bounded_quantum_meridian_transport.md` bounds particular Heisenberg meridian observables, not the varying scalar period. The tensor finite-jet and generic boundary-source estimates vary \(q\) with specified lifts and fixed main highest weight, rather than replacing it by \(d+s\). The bulk normal comparison in `quantum_normal_crossing_bulk_response.md` concerns specified nonvanishing flow charts before summation; its own scope excludes selected global periods and endpoints.

## 7. The first missing analytic lemma

There is no missing definition of the main-meridian scalar or of its regular remainder: (3)–(5) and (15) are exact finite sources. What is missing is a cancellation-preserving estimate for their contraction, compatible with the geometric complete block.

For a microscopic main-meridian statement, a concrete first target is a bound for \(\rho_N(z)\) on a fixed complex disk, in the actual normalization of (17), followed by identification of its selected limit. A termwise bound such as (7), a polynomial bound on each filter in (15), or the existing auxiliary-color packet does not furnish that bound. Even local boundedness alone supplies only subsequences; a source comparison is still needed to select their limit. The existing central-multiplier examples show why the root equation, ordinary values, and a qualitative exponential-type condition alone are insufficient.

For a fixed main-meridian neighborhood, the obligation is stronger. One needs an exact main-color Conway compiler or another source-preserving reduction that retains the moving nodes, the dual-color/cup data, the cutoff currents and the regularization filter; then one needs a uniform nonzero geometric packet and a bound on its complement in that new source. At \(s=0\) the complete module is self-dual; under \(\alpha=d+s\), its dual color is \(d-s\). Existing complete basis reversal and first Hermite normals cannot simply be declared to give this full two-color family.

The nearby-zero obstruction for the reduced family prevents replacing this obligation by a uniform nonzero ratio germ for \(F_N\) itself. It does not prove or disprove such a statement for the regular remainder. The scalar volume theorem at \(M=1\), and the exact pointed operator reconstruction there, remain unchanged.

The actionable continuation is therefore (15) together with the precise cut insertion (5): either recouple this whole filtered source into a geometric packet, or directly control its signed residue classes. No such control has been inferred in this report.
