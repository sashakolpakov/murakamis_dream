# The actual Casimir, crossing jets, and closing functional

Bounded independent source audit, 1 November 2026.

The audited base is public commit 2301771b66296cb7f2331938f1bfe0855719dd3d in /private/tmp/murakamis_dream-publication. During this read the parent added the direct Fourier proof at Appendix N, label uf:local-fourier, and its finite checker. Those two current files are included separately in the hash record. I changed no public file and ran no manuscript, guide, or aggregate builder.

The conclusion of this bounded audit is that the actual pair-Casimir annihilator, confluent crossing polynomial, inverse crossing, pivotal trace, and fixed-root Gaussian have consistent proofs at every integer level N at least 2. I found no missing prime-level, odd-level, semisimplicity, or coprimality assumption in these finite inputs. This is not an audit of the subsequent complex packet estimates or of a global volume theorem. In particular it does not supply an exponential estimate for a closed source.

## 1. Exact inputs and notation

Write \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and \(\rho=q-q^{-1}\). Thus \(q^N=-1\), \(Q\) has order exactly \(N\), and
\[
 [j]_q=\frac{q^j-q^{-j}}{q-q^{-1}}\ne0
 \quad(1\le j<N).
\]
The last assertion uses only primitivity and is valid at composite levels. Powers with a half-integral exponent use the specified exponential lift, rather than a newly chosen square root.

On the original color use
\[
 K v_j=q^{d-2j}v_j,\qquad Fv_j=v_{j+1},\qquad
 Ev_j=[j]_q^2v_{j-1},
\]
with missing endpoint vectors zero. The coproduct is
\[
 \Delta F=F\otimes1+K^{-1}\otimes F,\quad
 \Delta E=E\otimes K+1\otimes E,\quad
 \Delta K=K\otimes K.
\]
The normalized pair Casimir is
\[
 \Omega=\rho^2(\Delta F)(\Delta E)+q\Delta K+q^{-1}(\Delta K)^{-1}.
\]
The unbraided finite universal matrix will be denoted \(\mathcal R\), and the checked crossing \(B=P\mathcal R\). The direct-power notes denote this checked crossing by \(R\); their \(R^n\) is \(B^n\) in the present report. This distinction prevents a permutation from being silently lost in a functional-calculus statement.

Primary local anchors are:

- cyclic_steinberg_lattice.md, §1, lines 13–69: the regular family over \(\mathbb C[t,t^{-1}]\) and its original-color fiber;
- kashaev_crossing_and_period_lattice.md, §§1–3, lines 22–185: the literal finite crossing, Fourier comparison, and enhancement;
- casimir_braiding_and_recoupling_lattice.md, §3, lines 108–183, and §8, lines 377–430: generic tensor calculation, confluent derivative, and pivotal trace;
- actual_small_circle_polynomial_face_insertion.md, §§1–2, lines 15–100, and actual_signed_small_circle_face_kernel.md, §1, lines 9–95: physical endpoints and the polynomial face operator;
- actual_direct_long_power_source.md, §3, lines 127–152: the full crossing-power Gaussian;
- actual_spectral_total_derivative_source.md, opening through line 50, and actual_uniform_filling_supremum_bound.md, §§1–2: the actual spectral functional.

The original published crossing conventions were also checked against Kashaev's displayed definitions (2.7), (2.8), (2.12), and the displayed four-index enhanced crossing and enhancement in Murakami–Murakami §4. This check uses their definitions, not their comparison theorem: [Kashaev](https://arxiv.org/pdf/q-alg/9504020), [Murakami–Murakami](https://arxiv.org/pdf/math/9905075). Their enhanced crossing's explicit index formula agrees with \(P(\mathcal R^o)^{\mathsf T}\) under the local note's input-column convention; its enhancement is \(-q\) times the cyclic shift. One must compare the index formula, not infer a transpose convention from the name of the crossing.

## 2. Regular specialization gives the physical annihilator

There are two valid routes, and neither requires the singular relative recoupling matrix to remain invertible at the physical fiber.

For the generic route replace \(q\) by an indeterminate \(z\), keep the dimension \(N\) fixed, and use
\[
 Ev_j=[j]_z[d-j+1]_zv_{j-1},\quad Fv_j=v_{j+1},\quad
 Kv_j=z^{d-2j}v_j.
\]
For \(0\le k\le d\), the highest vector in total degree \(k\) is
\[
 h_k=\sum_{a=0}^k b_a v_a\otimes v_{k-a},\quad b_0=1,
 \qquad
 \frac{b_{a+1}}{b_a}
 =-\frac{[k-a]_z[d-k+a+1]_z}
 {[a+1]_z[d-a]_z z^{d-2k+2a+2}}.
\]
All displayed denominator quantum integers are generically nonzero. Their products telescope, giving
\[
 b_k=(-1)^k z^{-k(d-k+1)}.
\]
The highest weight is \(\lambda=2d-2k\). The elementary identity
\[
 E F^r h_k=[r]_z[\lambda-r+1]_z F^{r-1}h_k
\]
forces nonvanishing for \(r\le\lambda\). If \(F^{\lambda+1}h_k\) were nonzero, it would be a highest vector of negative highest weight. The same formula would then force all its successive \(F\)-images to be nonzero, contradicting nilpotence of \(F\) on this finite tensor product. Thus this generated module has exactly \(\lambda+1\) dimensions.

Its Casimir eigenvalue is
\[
 c_k(z)=z^{2N-1-2k}+z^{-2N+1+2k}.
\]
These \(N\) eigenvalues are distinct over the generic field, and the dimensions sum to \(N^2\). Therefore the original generic pair matrix satisfies
\[
 \left\{\prod_{k=0}^{N-1}(X-c_k(z))\right\}(\Omega(z))=0.
\]
Both its matrix entries and the coefficients of this monic polynomial are regular at \(z=q\). Specialization gives
\[
 \chi_N(\Omega)=0,\qquad
 \chi_N(X)=\prod_{k=0}^{N-1}(X-q^{2k+1}-q^{-2k-1})
          =2T_N(X/2)+2.
\]
Here \(T_N\) is the standard first-kind Chebyshev polynomial. To check its multiplicities directly, substitute \(X=w+w^{-1}\) and multiply by \(w^N\). Both sides become \((w^N+1)^2\). Substitution is injective on polynomials. The paired roots are double; the only unpaired root is \(-2\) when \(N\) is odd.

This establishes an annihilator of the actual \(N^2\)-dimensional matrix. No assertion that this physical matrix is cyclic, or that its characteristic polynomial equals \(\chi_N\), is necessary. The relative \(H_\tau\) in the lattice note has an independent cyclicity statement for \(\tau\ne0\); that statement alone would not justify the specialization through the singular CG chart. The regular generic matrix identity above does justify it.

## 3. The actual crossing and its nilpotent part

The finite universal matrix has coefficients
\[
 \mathcal R(z)=z^{H\otimes H/2}
 \sum_{r=0}^{N-1}
 \frac{z^{r(r-1)/2}(z-z^{-1})^r}{[r]_z!}E^r\otimes F^r.
\]
At \(q\), each denominator with \(r<N\) is nonzero. Its elementary coefficient recurrence gives coproduct intertwining, with the terminal terms killed by \(E^N=F^N=0\). Thus the checked crossing preserves the generic highest-weight summands above.

In the coefficient of \(v_0\otimes v_k\) in \(P\mathcal R h_k\), only the zero-th term on \(v_k\otimes v_0\) contributes. Multiplying that Cartan factor by the displayed \(b_k\) gives
\[
 \lambda_k(z)=(-1)^k z^{d^2/2-k(2N-1-k)}.
\]
The generic crossing is therefore the polynomial in \(\Omega(z)\) interpolating these values at the \(c_k(z)\).

Let \(h=2k+1<N\), \(l=N-1-k\), and \(A=q^h-q^{-h}\ne0\). The collisions are exactly these pairs. Their crossing values agree because
\[
 \frac{\lambda_l(q)}{\lambda_k(q)}
 =(-1)^{N-h}q^{-N(N-h)}=1.
\]
Differentiation with respect to \(\log z\), before specializing, gives
\[
 (c_k-c_l)'=-2NA,\qquad
 (\lambda_k-\lambda_l)'=\lambda_k(q)N(N-h).
\]
Therefore, after dividing by \(\lambda_0=q^{d^2/2}\), the normalized polynomial has
\[
 r_N(c_k)=\nu_k=(-1)^kq^{k(k+1)},\qquad
 r_N'(c_k)=-\nu_k\frac{N-h}{2(q^h-q^{-h})}.
\]
There is only a value condition at the odd simple root. Replacing each pair of interpolation rows by its value and divided-difference rows gives an invertible confluent Vandermonde matrix in the limit. This proves regularity of the interpolation coefficients, not merely agreement of limiting eigenvalues. Specializing the whole matrix identity proves
\[
 B=\lambda_0r_N(\Omega)
\]
on every generalized eigenspace, including its nilpotent part.

Since every \(\nu_k\ne0\), this polynomial is a unit modulo \(\chi_N\). Its inverse has values \(\nu_k^{-1}\) and derivatives \(-r_N'(c_k)/\nu_k^2\). For every integer \(n\), positive, zero, or negative,
\[
 (r_N^n)(c_k)=\nu_k^n,\qquad
 (r_N^n)'(c_k)=n\gamma_k\nu_k^n,
 \quad \gamma_k=-\frac{N-h}{2(q^h-q^{-h})}.
\]
This is normal recovery for the actual crossing. No division by a finite Gaussian sum or assumption that such a sum is nonzero enters it.

The auxiliary triangular interpolation in actual_signed_small_circle_face_kernel.md is a different generic-q family. Its root divided difference is nevertheless the same: its node derivative difference is \(2NA\), while its value derivative difference is \(-\nu_kN(N-h)\). The signs cancel to the preceding answer. Its explicit commutator identity (5) was checked here as a rational identity in independent \(q,I,K,L\), not by sampling roots. The boundary cases follow after clearing denominators. Hence that proof does not substitute a value-only auxiliary germ for the actual crossing germ.

## 4. Self-duality and the exact pivotal scalar

The matrix in kashaev_ado_pointing.md §2 is
\[
 Jv_j=(-1)^jq^{j(j-N)}v_{d-j}.
\]
Its successive coefficient ratio is \(-q^{2j+1-N}\). Direct use of the antipodes \(S(E)=-EK^{-1}\), \(S(F)=-KF\) proves that it identifies the module with its dual, and \(JKJ^{-1}=K^{-1}\).

The identity for the finite \(\mathcal R\) can also be checked entrywise. For an entry that raises the first index from \(j\) to \(j+a\), conjugating by \(J\otimes J\) contributes
\(q^{2a(j-k+a)}\). The difference of the two relevant Cartan exponents is exactly
\[
 \frac{H_jH_k-H_{j+a}H_{k-a}}2=2a(j-k+a),
 \qquad H_j=d-2j.
\]
The remaining factorial products agree by \([N-r]_q=[r]_q\). This gives
\(\mathcal R^{\mathsf T}=(J\otimes J)\mathcal R(J^{-1}\otimes J^{-1})\), including both endpoints. Thus the transposed dual crossing and the standard checked crossing have the same reduced scalar with their respective pivots; no matrix norm of the change of basis is being discarded.

For completeness, scalarity of the pivotal partial trace follows directly from the coproduct equations. If \(A\) commutes with \(\Delta E,\Delta F,\Delta K\), put
\(C=\operatorname{tr}_2((1\otimes K)A)\).
Taking the ordinary partial trace of \([A,\Delta E]=0\) gives \([C,E]=0\): the terms containing only the second-factor \(E\) cancel by cyclicity. Taking the \(K\)-weighted partial trace of \([A,\Delta F]=0\) gives \([C,F]=0\); use
\[
 A(K^{-1}\otimes1)
 =(K^{-1}\otimes K^{-1})A(1\otimes K)
\]
to cancel the two other terms by cyclicity. The relation with \(K\) follows from \([A,K\otimes K]=0\). The original color is simple: its \(K\)-eigenvalues are distinct and its adjacent \(E,F\) coefficients are nonzero. Therefore \(C\) is scalar.

For \(A=B\), evaluate this scalar on \(v_0\). Only the zero-th crossing term with second input \(v_0\) survives, giving
\[
 \operatorname{tr}_2((1\otimes K)B)=q^{d^2/2+d}I
             =\alpha_N I,\qquad
 \alpha_N=q^{(N^2-1)/2}.
\]
For \(B^{-1}\), the analogous calculation on \(v_d\) gives \(\alpha_N^{-1}\). Hence
\[
 \frac{\lambda_0}{\alpha_N}=-q=\kappa,
 \qquad \Phi_N(r_N)=\kappa^{-1},\quad
 \Phi_N(r_N^{-1})=\kappa.
\]
These equalities fix the writhe character, rather than defining a freely normalized trace.

The literature comparison's Fourier factors retain the same normalization. Its \(\gamma=Qq^{-d^2/2}\) satisfies \(\gamma\alpha_N=-q\). The diagonal and Fourier conjugations on traced factors cancel exactly; the open-factor conjugation cancels because the cut operator is scalar. The printed inverse discussed in the old crossing note is not used: the negative crossing is the actual inverse of the specified positive matrix.

## 5. Closing at the repeated roots

Let \(\Phi_N(f)I=\operatorname{tr}_2((1\otimes K)f(\Omega))\). At generic \(z\), the full pivotal trace on the elementary tensor decomposition gives
\[
 [N]_z\Phi_z(f)=\sum_{k=0}^{N-1}[2N-1-2k]_z f(c_k(z)).
\]
The partial trace itself is a regular matrix expression. For a colliding pair put \(c=q^h+q^{-h}\), \(A=q^h-q^{-h}\), and \(\rho=q-q^{-1}\). The two dimensions have values \(-A/\rho,A/\rho\). Their summed derivative is \(2Nc/\rho\); the derivative coefficient multiplying \(f'(c)\) is \(2NA^2/\rho\). Finally \([N]'_q=-2N/\rho\). Dividing these derivatives gives
\[
 \Phi_N(f)=-\sum_{2k+1<N}
       \{c_k f(c_k)+(c_k^2-4)f'(c_k)\}
       +\mathbf1_{N\text{ odd}}f(-2).
\]
The odd unpaired term is literally \([N]_z f(z^N+z^{-N})\), so its limit contributes only \(f(-2)\). It must not be folded into a double node. If the polynomial coefficients of \(f\) themselves vary regularly with \(z\), the extra coefficient derivatives cancel because the two zeroth-order dimensions sum to zero. This justifies using the regular crossing interpolation as well.

There is an independent resolvent check. At a double root write \(h(z)=\chi_N(z)/(z-c)^2\). The Chebyshev differential equation and its derivative give
\[
 h(c)=\frac{N^2}{4-c^2},\qquad
 \frac{h'(c)}{h(c)}=\frac{c}{4-c^2};
 \qquad \chi_N'(-2)=N^2\quad(N\text{ odd}).
\]
If \((z-\Omega)^{-1}=P_c/(z-c)+Q_c/(z-c)^2+\cdots\), then
\[
 Q_c=\frac{4-c^2}{N^2}V_N(c),\qquad
 P_c=\frac{(4-c^2)V_N'(c)-cV_N(c)}{N^2}.
\]
Consequently the actual multiplier functional on a scalar polynomial \(H\) is
\[
 \mathcal L_N^f(H)=
 \sum_{2k+1<N}\frac{(4-c_k^2)(fH)'(c_k)-c_k f(c_k)H(c_k)}{N^2}
 +\mathbf1_{N\text{ odd}}\frac{f(-2)H(-2)}{N^2}.
\]
It sends \(V_N\) to \(f(\Omega)\). Equivalently it is
\(\ell_{\chi_N}(\widetilde fH)=N^{-2}\Phi_N(\widetilde fH)\), where \(\widetilde f\) is the full Hermite multiplier. The untwisted top-coefficient functional \(\ell_{\chi_N}\) and the twisted functional \(\mathcal L_N^f\) are distinct; a scalar rescaling alone does not replace the multiplier for arbitrary crossing powers.

The complete-channel normalization also agrees at the odd node. For
\(L_N=(-1)^dU_{N-1}(\Omega/2)\),
\[
 L_N'(c)=\frac{(-1)^dN}{2\sin^2\phi},\qquad
 L_{N,a}=\frac{(-1)^d2}{N}V_N(c),\qquad
 L_{N,*}=\frac1N V_N(-2)\quad(N\text{ odd}).
\]
The channel multiplicity is two in the paired case and one in the odd simple case. Thus the positive-circle normalization gives the same
\((-1)^dH_{V_N(c_a)}=N^2B_{N,a}\) in both cases. There is no omitted factor two at \(-2\).

## 6. Every integral power is the stated fixed-root Gaussian

Let
\[
 K(z)=\operatorname{arccosh}(-z/2)^2,\quad
 \hbar=2\pi i/N.
\]
Use its branch holomorphic on \(\mathbb C\setminus[2,\infty)\), with the removable value at \(-2\). Every node lies in this domain. At a paired node put \(\phi=\pi(2a+1)/N\) and \(s=d-2a\). Direct differentiation gives
\[
 K(c_a)=-\pi^2s^2/N^2,\qquad
 K'(c_a)=-\frac{\pi s}{N\sin\phi}.
\]
The elementary exponent identity
\[
 \frac{d^2+s^2}{4}-\frac{d^2}{2}-a(a+1)=-aN
\]
proves the exact value, including \((-1)^a\). Also
\[
 \frac{n}{2\hbar}K'(c_a)
 =-\frac{ns}{4i\sin\phi}=n\gamma_a.
\]
Thus both the values and first derivatives of
\(q^{nd^2/4}\exp(nK(z)/(2\hbar))\) agree with \(B^n\). The odd simple value agrees as well. Full Hermite functional calculus, using the proved matrix annihilator, yields
\[
 B^n=q^{nd^2/4}\exp\{nK(\Omega)/(2\hbar)\}
 \qquad(n\in\mathbb Z).
\]
This includes \(n=0\) and negative powers. It is a fixed-root identity and makes no claim that \(B\) is unitary or that a scalar Gaussian diagonalization controls the matrix norm. Its nilpotent exponential is essential.

## 7. The newly written direct Fourier adapter

I read Appendix N, label uf:local-fourier, and repro/check_local_face_fourier.py in their current form. The new proof is an independent finite route to the annihilator and local homogeneous source identity.

The balanced basis is \(e_i=v_i/(Q;Q)_i\). Its lowering coefficient is correct because
\[
 \frac{\rho^2[i]_q^2}{1-Q^i}=Q^{-i}-1.
\]
Thus the displayed \(\mathcal E\) is \(\rho^2E\), not \(E\). Expanding the coproduct gives exactly
\[
 D=2qU+2q^{-1}V^{-1}-(q+q^{-1})U/V,
\quad A_+=(V^{-1}-1)(1-QU),
\quad A_-=(Q^{-1}V^{-1}-1)(1-U).
\]
The four physical endpoint zeros occur before any grouping by residues.

For residue \(s\), set \(x=Q^{s+1}y\), \(b_u=-q^{-1}xQ^{-u}\), \(\mathsf E_{uj}=b_u^j\), and \(G_{uu}=q^{du}\). Substitution into the three face-operator coefficients gives \(-D,q^{-1}A_+,qA_-\). Since \(q^d=-q^{-1}\), this is
\[
 \mathsf E T\mathsf E^{-1}=-G^{-1}\Omega_s^{\mathsf T}G.
\]
The transpose is necessary. The inverse evaluation matrix is exactly
\((\mathsf E^{-1})_{jr}=N^{-1}b_r^{-j}\), so for any polynomial multiplier
\[
 (f(\Omega_s))_{ru}
 =N^{-1}q^{-d(r-u)}c^{-d}H_f(x,b,c,y),\quad b=b_u,\ c=b_r.
\]
The factor \(N^{-1}\), integer displacement, and degree-\(d\) homogeneous definition all agree with the original source. At even levels replacing \(r-u\) by its residue can change the sign. The proof correctly retains the canonical displacement and kills attempted physical wraps before using the Fourier transform. It does not claim this phase is residue-periodic.

The new checker forms the physical matrix from the four coproduct factors, separately from the three-band polynomial matrix. It tests a multiplier of degree \(N+1\), wrong-unwrapped-total zeros, and an intentionally incorrect residue-phase choice. These are meaningful bounded discriminators of normalization and support. I read its code but did not rerun it; the parent reports its execution. Its finite-field examples are not a proof at every complex root. The written conjugacy above is that proof.

## 8. Limits and recommendations

No essential correction to the audited finite input is requested. The following distinctions must remain explicit in any import:

1. The cyclic lattice lives over nonzero parameters; regularity at the physical fiber means \(t=1\), not an assertion about an \(X^{-1}\)-formula at \(t=0\).
2. The generic relative cyclic Casimir and the physical nilpotent tensor need not have the same cyclic module structure. Use a regular matrix identity or the direct Fourier conjugacy for the physical annihilator.
3. Confluent crossing data are proved by regular divided differences of the specified matrix. Nodal values alone would leave its nilpotent normal undetermined.
4. The odd simple root has its value term and no independent derivative condition.
5. The local face identity retains canonical integer heads. Even-level phase signs are not residue-periodic before the global lifted face factors cancel.
6. Gaussian functional calculus is at the fixed root with its stated branch; it is not a generic-q continuation or a unitary bound.
7. The actual filling functional contains the Hermite multiplier. The abstract top-coefficient/remainder result does not identify arbitrary crossing powers by a scalar normalization alone.
8. The local algebra does not commute Casimirs at adjacent boxes. Multilinear insertion into the original source is legitimate; arbitrary reordering of coupons is not.
9. The original flat-plat homogeneous theorem and the separate general Morse adapter have distinct global scope. The local proof audited here does not by itself establish the latter's cup/cap count or topological realization.
10. No full-minus-central exponential bound, complex interpolant norm, nonzero global amplitude, or geometric volume identification follows solely from these finite identities.

The only computation executed for this report is the private exact symbolic check md-casimir-crossing-symbolic-check.py. It verifies six rational/polynomial identities, including the auxiliary commutator and three physical shift coefficients. It samples no levels. I did not rerun the pre-existing matrix diagnostics or the new Fourier runner. The companion JSON records exact file hashes, commands, and this scope.
