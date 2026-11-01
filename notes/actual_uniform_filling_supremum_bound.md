# Uniform bounds for inserting twist powers

The finite formula for a diagram can be organized in two steps. First, take the prescribed coefficient in its shared face variables. This gives a polynomial \(S_N\) in one spectral variable for each crossing region. Then apply a linear functional in each spectral variable to insert the chosen signed twist power.

This note bounds the second step. Inserting \(n\) crossings costs at most \(1+|n|/2\) in the supremum norm on the real spectral interval, independently of the quantum level \(N\). There is a stronger estimate for the two one-sided pieces of the local polynomial: their values vanish at all spectral nodes, and the cost is then at most \((N-1)/N\), independently of \(n\) as well. The derivatives at repeated nodes remain in the calculation.

The estimate applies after the face coefficient has been taken. All crossing regions therefore retain their common face constraints. To obtain a volume theorem from it, one must still bound this shared polynomial and prove that the geometric contribution survives.

Here is the precise statement. Let \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and let \(\mathcal L_N^{n}\) be the full-Hermite functional for the actual crossing power \(R^n\), with \(n\in\mathbb Z\), defined below. For a polynomial \(H\) of degree at most \(d\),
\[
 |\mathcal L_N^{n}H|
       \le \left(1+\frac{|n|}{2}\right)
                         \|H\|_{[-2,2]}.
 \tag{1}
\]
If \(H\) vanishes at every root of \(\chi_N(z)=2T_N(z/2)+2\), including the simple root \(-2\) when \(N\) is odd, the stronger bound is
\[
 |\mathcal L_N^{n}H|\le \frac dN\|H\|_{[-2,2]}.
 \tag{2}
\]
Vanishing means values only; the derivatives at double roots are retained.

For \(r\) crossing regions, let \(S(\sigma_1,\ldots,\sigma_r)\) have degree at most \(d\) in each variable. Suppose that for every \(e\) in a set \(J\), \(S\) vanishes whenever \(\sigma_e\) is a spectral node, with its other variables arbitrary. Then
\[
 \left|\left(\bigotimes_{e=1}^r\mathcal L_N^{n_e}\right)S\right|
 \le \left(\frac dN\right)^{|J|}
       \prod_{e\notin J}\left(1+\frac{|n_e|}{2}\right)
                          \|S\|_{[-2,2]^r}.
 \tag{3}
\]
In particular this applies to each term containing a specified lower or upper one-sided factor, with \(J\) its one-sided crossing regions. The case \(J=\varnothing\) is the full-source bound.

There is also a bound for the whole complementary source without expanding it into sectors. Let \(\mathcal D\) have degree at most \(d=N-1\) in each spectral variable. If it vanishes on the Cartesian product of all spectral node sets, then
\[
 \left|\left(\bigotimes_{e=1}^r\mathcal L_N^{n_e}\right)\mathcal D\right|
 \le \left\{\prod_e\left(1+\frac{|n_e|}{2}\right)
       -\prod_e\left(\frac1N+\frac{|n_e|}{2}\right)\right\}
                         \|\mathcal D\|_{[-2,2]^r}.
 \tag{4}
\]
For the actual numerator one may take
\(\mathcal D=S_{\mathrm{full}}-S_{\mathrm{CROSS}}\).
The coefficient in braces has degree at most \(r-1\) in the quantities \(|n_e|\): the highest product cancels exactly. None of (1)–(4) assumes positivity of spectral coefficients, asymptotic localization, or dominance of a Fourier charge.

## 1. The exact source and its normalization

Use the original pair Casimir \(\Omega\), not an operator reconstructed from its spectral values. It satisfies \(\chi_N(\Omega)=0\), and polynomial division gives the degree-\(d\) resolvent numerator
\[
 V_N(z;\Omega)=\chi_N(z)(z-\Omega)^{-1}.
 \tag{5}
\]
The right side means the resulting matrix polynomial, including at every spectral node. It is not the determinant adjugate of the full \(N^2\)-dimensional matrix.

The [original homogeneous face source](actual_homogeneous_casimir_face_source.md) associates to (5) a four-face polynomial \(H_V(x,b,c,y;z)\), with literal input/output middle faces \(b,c\). Fix a connected original diagram at \(N\ge3\), with its actual cups, caps, unrestricted marked cap, protected face targets, and every ordered box. The applications include connected flat plats and the connected matched simple-sphere Morse diagrams of [the general Morse source theorem](research_matched_sphere_morse_source.md), §§1,5–6, and [the terminal-fan source proof](actual_balanced_terminal_fan_volume.md), §§5–7. For the latter, the actual cyclic orders and crossing-disk frames are retained, and the marked main edge determines the two protected faces. The exact coefficient identity is the only input here: no complete-radius balance or geometric certificate is required for this finite norm estimate. The shared spectral polynomial is
\[
 S_N(\boldsymbol\sigma)=
 [\textstyle\prod_{f\ \mathrm{ordinary}}L_f^d]
       \prod_{e=1}^{r}H_V(L_{x_e},L_{b_e},L_{c_e},L_{y_e};\sigma_e),
 \tag{6}
\]
with the two protected face exponents zero. Every variable \(\sigma_e\) has degree at most \(d\). The original marked source after inserting the signed powers is exactly
\[
 Z_N(\boldsymbol n)=
        \left(\bigotimes_{e=1}^r\mathcal L_N^{n_e}\right)S_N.
 \tag{7}
\]
The face-grid factors, cup/cap factors and the original \(N^{-1}\) marked scalar have already canceled as in those source theorems; there is no additional \(N^r\) in (7). Thus \(Z_N\) is the original reduced ribbon contraction. Conversion to the prescribed zero-framed enhanced Kashaev convention uses the recorded framing/component character, of modulus one at complete color; for a knot the enhanced component sign is one. In the specified full one-cut modified convention, retain the additional factor \(i^{N+3}/N\). Original exterior Cartan and framing factors remain in their prescribed locations throughout. These are the physical normalization choices; no new quantum dimension or color average is introduced by the norm theorem.

The polynomial degree and the identities (5)–(7), rather than a hypothesis about arbitrary polynomial solutions of a recurrence, are the source assumptions used here. The scalar inequalities (1)–(4) themselves hold for every polynomial of the indicated degree and every \(N\ge2\).

## 2. Repeated roots, the odd simple root, and the midpoint identity

Write
\[
 c_a=2\cos\frac{(2a+1)\pi}{N},\qquad
 0\le a<\lfloor N/2\rfloor.
 \tag{8}
\]
These are the distinct double roots. The only remaining root is \(-2\), simple, when \(N\) is odd. At a double root \(c\), put \(h(z)=\chi_N(z)/(z-c)^2\). The Chebyshev differential equation gives
\[
 h(c)=\frac{N^2}{4-c^2},\qquad
 \frac{h'(c)}{h(c)}=\frac{c}{4-c^2};
 \qquad \chi_N'(-2)=N^2\quad(N\ \mathrm{odd}).
 \tag{9}
\]
Indeed \((4-z^2)\chi_N''-z\chi_N'+N^2(\chi_N-2)=0\). Evaluate it and its derivative at \(c\), using \(\chi_N(c)=\chi_N'(c)=0\), to obtain (9).

If the resolvent at \(c\) is \(P_c/(z-c)+Q_c/(z-c)^2\), then \(V_N(c)=h(c)Q_c\) and \(V_N'(c)=h(c)P_c+h'(c)Q_c\). Consequently the [original spectral derivative functional](actual_spectral_total_derivative_source.md), on any scalar entry \(H\), is
\[
 \mathcal L_N^fH=
 \sum_a\frac{(4-c_a^2)(fH)'(c_a)-c_af(c_a)H(c_a)}{N^2}
 +\mathbf1_{N\ \mathrm{odd}}\frac{f(-2)H(-2)}{N^2}.
 \tag{10}
\]
It sends \(V_N\) to \(f(\Omega)\), with \(f'(c)Q_c\) included. The prime in (10) is a derivative in \(z\).

Let
\[
 \phi_k=\frac{(2k+1)\pi}{N},\quad 0\le k<N,\qquad
 P(\phi)=H(2\cos\phi).
 \tag{11}
\]
Each double root appears twice in this grid. At the odd simple root, \(\phi=\pi\) occurs once, and differentiating the sine supplies exactly its weight in (10). Thus (10) is equivalently
\[
 \mathcal L_N^fH
 =-\frac1{2}\sum_{k=0}^{N-1}
       \left.\frac{d}{d\phi}
       \frac{2\sin\phi\,f(2\cos\phi)H(2\cos\phi)}{N^2}
       \right|_{\phi=\phi_k}.
 \tag{12}
\]
There is no omission or doubling of the odd simple node.

For the actual positive or negative integral crossing power, the [full-Hermite Gaussian](actual_direct_long_power_source.md) is
\[
 f_n(2\cos\phi)=q^{nd^2/4}
          \exp\left(\frac{inN(\phi-\pi)^2}{4\pi}\right),
 \qquad 0\le\phi\le2\pi.
 \tag{13}
\]
Here \(q^a\) means \(e^{\pi ia/N}\), fixing the original square-root lift even for nonintegral \(a\). In particular
\[
 |f_n|=1,\qquad |\partial_\phi f_n|\le\frac{|n|N}{2},\qquad
 f_n(c_a)=q^{nd^2/2}(-1)^{an}q^{na(a+1)}.
 \tag{14}
\]
The nodal phase is the actual crossing phase, not its absolute value substituted into the source. Formula (13) is symmetric about \(\pi\); it has the required holomorphic germ at the odd simple node. The possible endpoint cut at \(z=2\) does not occur at a spectral node and does not enter the finite identity (12).

Expanding (12), with primes now in \(\phi\), gives
\[
 \mathcal L_N^{n}H=-\frac1{N^2}\sum_{k=0}^{N-1}
       \bigl(\cos\phi_k f_kP_k+
        \sin\phi_k f_k'P_k+\sin\phi_k f_kP_k'\bigr).
 \tag{15}
\]
This finite formula is sufficient for every norm below; no interchange of an infinite Fourier series or a contour limit is needed.

## 3. An elementary exact derivative inequality

For every complex trigonometric polynomial \(P\) of degree at most \(d\ge1\), set \(\theta_j=(2j-1)\pi/(2d)\), \(1\le j\le2d\). The finite Riesz interpolation identity is
\[
 P'(x)=\sum_{j=1}^{2d}
       \frac{(-1)^{j+1}}{4d\sin^2(\theta_j/2)}P(x+\theta_j).
 \tag{16}
\]
For completeness, invert the finite Fourier matrix on modes \(-d+1,\ldots,d\). If \(z=e^{-i\theta_j}\), so \(z^{2d}=-1\), differentiating the finite geometric sum gives its weight
\[
 \frac1{2d}\sum_{\ell=-d+1}^{d}i\ell e^{-i\ell\theta_j}
 =\frac{i z^{-d+1}}{d(1-z)^2}
 =\frac{(-1)^{j+1}}{4d\sin^2(\theta_j/2)}.
 \tag{17}
\]
The extra mode \(-d\) has samples opposite to those of \(d\), and its derivative at zero is opposite too. Thus (16) holds on all modes \(-d,\ldots,d\); translation gives arbitrary \(x\).

The elementary sine product
\(\prod_{j=0}^{2d-1}\sin(x+j\pi/(2d))=C_d\sin(2dx)\), with \(C_d\ne0\), yields after two logarithmic derivatives and substitution \(x=\pi/(4d)\)
\[
 \sum_{j=1}^{2d}\frac1{4d\sin^2(\theta_j/2)}=d.
 \tag{18}
\]
Taking absolute values in (16) therefore proves
\[
                  \|P'\|_{\mathbb R}\le d\|P\|_{\mathbb R}.
 \tag{19}
\]
The argument works without real coefficients or positivity.

The same finite identity and triangle inequality hold when the coefficients lie in any finite-dimensional normed space. Thus (19), and consequently (1)–(4), hold for such vector-valued polynomials without a dimension factor. The intended application here remains the original shared scalar coefficient (6); no change of the source norm is required.

## 4. Full and vanishing-node bounds

Since \(H\) has degree at most \(d\), \(P(\phi)=H(2\cos\phi)\) has trigonometric degree at most \(d\), and its supremum is exactly \(\|H\|_{[-2,2]}\). Equations (14), (15), and (19) give
\[
 |\mathcal L_N^{n}H|
 \le\frac{N}{N^2}\left(1+\frac{|n|N}{2}+d\right)\|H\|
 =\left(1+\frac{|n|}{2}\right)\|H\|,
 \tag{20}
\]
because \(d+1=N\). This proves (1).

If \(H\) vanishes at every node, the first two terms of (15) vanish exactly. Only the derivative of the original numerator remains. Applying (19) to that term gives (2), uniformly in every signed \(n\), including zero.

Here is why the original lower and upper one-sided numerators satisfy this hypothesis. Put
\(D_-(z)=\prod_{a=0}^{\lfloor N/2\rfloor-1}(z-c_a)\).
The exact lower-row restriction leaves the factor
\[
 \frac{\chi_N(z)}{D_-(z)}=
 \begin{cases}D_-(z),&N\ \mathrm{even},\\
 (z+2)D_-(z),&N\ \mathrm{odd}.
 \end{cases}
 \tag{21}
\]
Every lower one-sided entry is divisible by (21); literal row reflection gives the same statement for the upper piece. Thus values vanish at all nodes. On the lower invariant block \(\Omega_-\), whose eigenvalues \(c_a\) are distinct, (10) reduces exactly to
\[
 \mathcal L_N^nH_{V,\mathrm L}
 =\sum_a f_n(c_a)\frac{4-c_a^2}{N^2}
                       H_{V,\mathrm L}'(c_a).
 \tag{22}
\]
These numerator derivatives are the original lower-block spectral projectors. The derivative of \(f_n\) disappears, but the semisimple source is not zero. For example the literal local diagonal coefficient obeys
\[
 [c^d]H_{V,\mathrm L}(z)=\frac{\chi_N(z)}{z-c_0},
 \qquad [c^d]H_{R^n,\mathrm L}=q^{nd^2/2}.
 \tag{23}
\]
Its modulus is one. This is an actual local coefficient, not a claim that the same boundary can maximize a closed source.

## 5. Shared polynomials and the unsplit complementary source

The other finite functionals preserve each partial node-vanishing condition. Applying (1) and (2) successively to the original shared polynomial proves (3). Coefficient extraction in (6) is performed first and is never replaced by independent local maximization.

For clarity, (4) needs only joint grid vanishing, not vanishing on every node hyperplane. In each coordinate (15) is a sum of an evaluation term and a term differentiating \(P\). Before summing its \(N\) grid entries, the two coefficient bounds are \(1+|n_e|N/2\) and \(1\), respectively. For a subset \(A\) of differentiated variables, iterating (19) gives
\[
 \|\partial_A\mathcal D(2\cos\boldsymbol\phi)\|
                  \le d^{|A|}\|\mathcal D\|_{[-2,2]^r}.
 \tag{24}
\]
The term \(A=\varnothing\) vanishes pointwise at the tensor grid. Every other term is bounded by
\(\prod_{e\in A}(d/N)\prod_{e\notin A}(1/N+|n_e|/2)\|\mathcal D\|\).
Adding the nonempty subsets proves (4).

In the [original central-cut decomposition](actual_cross_cofactor_factorization.md), the lower and upper pieces have the factor (21). The full numerator is the sum of those pieces and the central crossing piece, denoted CROSS in the source formulas. At odd levels the central row belongs to that crossing piece. Hence every local full numerator agrees with CROSS at every spectral node. Multiplication and the one original shared coefficient extraction show
\[
 (S_{\mathrm{full}}-S_{\mathrm{CROSS}})
                    (c_{a_1},\ldots,c_{a_r})=0
 \tag{25}
\]
for all choices of nodes, including odd simple nodes. Applying (4) to this unsplit difference avoids summing the absolute values of exponentially many path terms. The statement is finite and exact even though its remaining shared supremum can be large.

## 6. What the norm theorem does and does not supply

There is already a level-independent dual filling cost in the [positive Fourier–Hermite Gram construction](actual_filling_fourier_hermite_gram.md): its squared Hilbert dual norm is exactly \(1+n^2(N^2-1)/(12N^2)\). That theorem uses a specified positive energy of the entire mixed-color packet. The present bounds use instead the supremum of the original shared resolvent numerator. The additional statements here are the twist-independent vanishing-node estimate and the unsplit product-grid cancellation. Neither construction by itself supplies the geometric exponential bound for its remaining source norm.

For a fixed diagram and fixed powers, all constants in (1)–(4) are independent of \(N\). Thus any sharp exponential estimate for the same shared spectral supremum passes to its actual filled source without a new exponential cost. The theorem also shows precisely where a derivative of the crossing phase drops out and why this saves one or more twist factors.

It does not prove that \(\|S_N\|\), or the complementary norm in (4), grows at the geometric volume rate. Neither node vanishing nor the uniform functional norm controls this remaining between-node polynomial. Separate absolute local envelopes may exceed that rate, and (23) prevents an argument that every one-sided channel is identically killed. The theorem asserts no new saddle dominance, peripheral representation, or knot-volume equality.

The finite reproduction `experiments/audit_actual_uniform_filling_supremum_bound.py` takes `--repo` pointing to the research checkout. It checks the Chebyshev double/simple-root identities at levels 2–12 and the Riesz formula at degrees 1–12 exactly in cyclotomic fields. It also compares the midpoint reconstruction with independently built original coproduct/Casimir and signed braid matrices at levels 3–8, for powers \(\pm1,\ldots,\pm5\), and checks the lower-block compression including its normal data. The JSON output distinguishes the exact rational cyclotomic calculations from exact finite-field matrix checks. These finite cases check algebraic identities; the all-level inequalities follow from the proofs above, not from sampled norm ratios.


## 7. The estimate needed for long fillings

It is useful to state the remaining comparison with its quantifiers. Fix the diagram, and write
\[
 \mathcal D_N=S_{N,\mathrm{full}}-S_{N,\mathrm{CROSS}}.
\]
This polynomial does not depend on the twist powers. Suppose one proves, for some fixed \(\eta>0\),
\[
 \|\mathcal D_N\|_{[-2,2]^r}
       \le \exp\bigl(N(\Phi-\eta)+o(N)\bigr).
 \tag{26}
\]
Here \(\Phi\) is the complete augmented action in the normalization of the source. When it is identified geometrically, \(\Phi=\operatorname{Vol}(M_{\mathrm{aug}})/(2\pi)\).

For each fixed tuple \(\boldsymbol n\), equation (4) then gives
\[
 \left|\left(\bigotimes_e\mathcal L_N^{n_e}\right)\mathcal D_N\right|
       \le \exp\bigl(N(\Phi-\eta)+o(N)\bigr).
 \tag{27}
\]
The finite factor in (4) is absorbed in \(o(N)\); this argument does not claim uniformity in twist powers growing with \(N\).

Suppose separately that the crossing contribution has a nonzero asymptotic
\[
 Z_{N,\mathrm{CROSS}}(\boldsymbol n)
       =a_N\exp(N\mathcal A_{\boldsymbol n}),\qquad
       N^{-1}\log|a_N|\longrightarrow0,
 \tag{28}
\]
where \(\Re\mathcal A_{\boldsymbol n}>\Phi-\eta\). Equations (27) and (28) show that the complementary contribution divided by the crossing contribution tends to zero exponentially. Consequently
\[
 \lim_{N\to\infty}N^{-1}\log|Z_N(\boldsymbol n)|
       =\Re\mathcal A_{\boldsymbol n}.
 \tag{29}
\]
The subexponential normalization factors in section 1 preserve this limit. Identifying \(2\pi\Re\mathcal A_{\boldsymbol n}\) with the hyperbolic volume still requires the geometric filling argument for that diagram.

This implication explains why a strict gap in (26) is useful for sufficiently long fixed fillings. The desired filled action approaches the augmented action as the auxiliary fillings become long. A bound for the full twist-independent polynomial at the augmented rate alone would give only that larger rate; it would not prove the smaller filled volume. The norm theorem proves the passage from (26) to (27). It does not prove (26) or supply (28) for a new diagram.
