# An exact local adapter from the division-free braid to the Newton algebra

Written derivation, 14 November 2026. The external formulas are those of
[rivin-jones, commit e956fb919ac7d1bbc7cb3d3873fbac993feb94b7](https://github.com/igorrivin/rivin-jones/tree/e956fb919ac7d1bbc7cb3d3873fbac993feb94b7),
in `docs/MATHEMATICS.md` and `python/rivin_jones/r_matrix.py`.
Only their written formulas are used. No external code was imported,
executed or used for a numerical calculation.

There is an explicit regular change of strand coordinates. With the
external choice \(A_N=e^{-\pi i/(2N)}\), it reverses the crossing sign:
the external positive crossing becomes our literal negative crossing.
The change is unitary at this root. Restriction to a specified cyclic
middle-weight space then identifies the full Newton regular module,
including every first normal at a repeated Casimir root. This is not
a compression of an arbitrary \(N^2\)-dimensional operator to \(N\)
coordinates.

## 1. A generic strand adapter and a coefficient proof

Fix \(N\ge2\), put \(d=N-1\), and first take a generic nonzero \(A\).
Set
\[
 \zeta=A^{-2},\qquad \zeta^{1/2}=A^{-1},\qquad
 \rho_\zeta=\zeta-\zeta^{-1},\qquad h_i=d-2i.
\]
The specified square-root lift is used in every Cartan factor.
Write \([a]=[a]_\zeta\), \([a]!=\prod_{r=1}^a[r]\), and
\(F_a=(\zeta^2;\zeta^2)_a\). On the ordinary physical module take
\[
 E v_a=[a][N-a]v_{a-1},\qquad Fv_a=v_{a+1},
 \qquad Kv_a=\zeta^{h_a}v_a.
\]
The balanced coordinates are
\[
 |a\rangle_\zeta=\frac{\rho_\zeta^a}{F_a}v_a.
 \tag{1}
\]
They agree at \(\zeta=q=e^{\pi i/N}\) with the balanced coordinates
of [the physical pair algebra](../papers/newton-calculus/finite.tex).
Every denominator in (1) is nonzero near that root.

Let \(e_i\) denote the external strand basis and define
\[
 T_A e_i=\zeta^{-i(i-1)/2}|d-i\rangle_\zeta
          =A^{i(i-1)}|d-i\rangle_\zeta.
 \tag{2}
\]
As a matrix from external coordinates to balanced coordinates this is
an invertible anti-diagonal monomial matrix, regular for every nonzero
\(A\). Let \(R^{\rm ext}_\pm(A)\) be the displayed external crossings,
and let \(R^{\rm bal}_+(\zeta)\) be the physical braided universal
crossing \(P\mathscr R\), with its full Cartan factor, in (1).
This is the self-dual convention explicitly identified with the
physical Casimir polynomial in
[the Casimir crossing comparison](casimir_braiding_and_recoupling_lattice.md),
Section 3.

**Proposition 1.** In a neighborhood where the displayed finite
factorials are nonzero,
\[
 (T_A\otimes T_A)R^{\rm ext}_-(A)
                  (T_A\otimes T_A)^{-1}=R^{\rm bal}_+(\zeta),
 \qquad
 (T_A\otimes T_A)R^{\rm ext}_+(A)
                  (T_A\otimes T_A)^{-1}=R^{\rm bal}_+(\zeta)^{-1}.
 \tag{3}
\]
There is no additional scalar in these identities.

*Proof.* In the spin coordinates \(w_a=v_a/[a]!\), the two ordinary
operators have coefficients
\[
 Ew_a=[N-a]w_{a-1},\qquad Fw_a=[a+1]w_{a+1}.
\]
The finite universal formula therefore gives the coefficient from
\((i,j)\) to \((j+k,i-k)\) as
\[
 \zeta^{(h_i+2k)(h_j-2k)/2+k(k-1)/2}\rho_\zeta^k
 \frac{[d-i+k]!}{[d-i]!}
 \frac{[j+k]!}{[j]![k]!}.
 \tag{4}
\]
The allowed range is \(0\le k\le\min(i,d-j)\). This follows by
applying the \(E^k\otimes F^k\) term and then the Cartan factor and
exchange; it is an entry calculation in the universal crossing.

The change from spin coordinates to (1) is diagonal with entries
\[
 C_a=\frac{F_a}{\rho_\zeta^a[a]!}
       =(-1)^a\zeta^{a(a+1)/2}.
\]
Its output/input ratio in (4) is
\(\zeta^{k(j-i+k)}\). Thus the balanced positive coefficient is
\[
 \zeta^{h_i h_j/2-k(j-i+k)+k(k-1)/2}\rho_\zeta^k
 \frac{[d-i+k]!}{[d-i]!}
 \frac{[j+k]!}{[j]![k]!}.
 \tag{5}
\]

Now use external input \((I,J)\). Its negative crossing goes to
\((J-k,I+k)\), with \(0\le k\le\min(J,d-I)\). In the external
formula \(A^2=\zeta^{-1}\), so the symmetric Gaussian binomial is
\([I+k]!/([I]![k]!)\). Each product factor is
\(-\rho_\zeta[d-J+r]\). Those signs cancel the explicit
\((-1)^k\). The coefficient is consequently
\[
 \zeta^{h_Ih_J/2+k(k-1)/2}\rho_\zeta^k
 \frac{[d-J+k]!}{[d-J]!}
 \frac{[I+k]!}{[I]![k]!}.
 \tag{6}
\]
Under (2) the physical input is \(i=d-I,j=d-J\), and the output
is \((j+k,i-k)\). The adapter's output/input ratio is
\[
 \zeta^{-k(I-J+k)}=\zeta^{-k(j-i+k)}.
\]
Also \(h_Ih_J=h_i h_j\). The factorial products in (6) become
exactly those in (5), and the allowed ranges agree. This proves the
first identity entry by entry.

For completeness the inverse assertion can be checked before
specialization. In the external spin coordinates put \(t=A^2\),
\(X=E\otimes F\), and \(D=t^{H\otimes H/2}\). The unbraided
positive crossing is \(D\sum_{k<N}a_kX^k\), where
\[
 a_k=\frac{t^{k(k-1)/2}(t-t^{-1})^k}{[k]_t!}.
\]
Its inverse is \(\sum_{k<N}b_kX^kD^{-1}\), where
\[
 b_k=\frac{(-1)^k t^{-k(k-1)/2}(t-t^{-1})^k}{[k]_t!}.
\]
Indeed, writing \(Q_t=t^2\) and \(z=(t-t^{-1})(1-Q_t)\), these
coefficients are respectively
\(Q_t^{k(k-1)/2}z^k/(Q_t;Q_t)_k\) and
\((-1)^kz^k/(Q_t;Q_t)_k\). Their coefficient convolution at each
\(1\le m<N\) vanishes by the finite Gaussian identity
\(\sum_{j=0}^m(-1)^jQ_t^{j(j-1)/2}{m\brack j}_{Q_t}
=\prod_{r=0}^{m-1}(1-Q_t^r)=0\). Since \(X^N=0\), this proves
the inverse identity. After the exchange the inverse goes from
\((I,J)\) to \((J-k,I+k)\); its coefficient is exactly the external
negative formula, including its input Cartan factor. Taking the
inverse of the first identity in (3) proves the second. \(\square\)

The same calculation also fixes the trace weight and pinned strand:
\[
 T_A K_{\rm ext}T_A^{-1}=K,\qquad T_Ae_0=|d\rangle_\zeta,
 \quad K_{\rm ext}e_i=A^{2h_i}e_i.
 \tag{7}
\]
Thus the external highest-weight pin becomes the physical lowest
coordinate. Replacing that coordinate by another one requires the
scalarity of the actual partially traced endomorphism; it is not an
identity for an arbitrary open matrix.

## 2. Root specialization retains the entire crossing polynomial

Specialize \(A=A_N\), \(\zeta=q=e^{\pi i/N}\), and write \(T_N=T_{A_N}\).
Every entry on the anti-diagonal of \(T_N\) has modulus one. Hence
\(T_N\) is unitary for the coordinate Euclidean norms, and (3)
introduces no norm amplification in those strand coordinates.

Keep the actual physical pair Casimir \(\Omega\) and define
\[
 \Omega_{\rm ext}=(T_N\otimes T_N)^{-1}\Omega(T_N\otimes T_N).
\]
The physical pair calculation gives
\[
 P_N(\Omega)=0,\qquad P_N(z)=2T_N^{\rm Cheb}(z/2)+2,
 \qquad R^{\rm bal}_+(q)=\kappa r_N(\Omega),
 \quad \kappa=q^{d^2/2},
\]
where the superscript distinguishes the Chebyshev polynomial from
the coordinate adapter. Therefore (3) gives exact full-pair identities
\[
 R^{\rm ext}_+(A_N)=\kappa^{-1}r_N(\Omega_{\rm ext})^{-1},
 \qquad
 R^{\rm ext}_-(A_N)=\kappa r_N(\Omega_{\rm ext}).
 \tag{8}
\]
The inverse in (8) is the inverse in the full quotient
\(\mathcal A_N=\mathbb C[z]/(P_N)\).

For specificity, at a double node
\(c_j=q^{2j+1}+q^{-2j-1}\), choose \(2j+1<N\). Put
\[
 \nu_j=(-1)^j q^{j(j+1)},\qquad
 \alpha_j=\frac{r_N'(c_j)}{\nu_j}
       =\frac{i(d-2j)}{4\sin((2j+1)\pi/N)}.
\]
On \(\mathbb C[\varepsilon]/(\varepsilon^2)\), (8) is multiplication by
\[
 \kappa^{-1}\nu_j^{-1}(1-\alpha_j\varepsilon)
 \quad\hbox{or}\quad
 \kappa\nu_j(1+\alpha_j\varepsilon),
 \tag{9}
\]
respectively. Neither normal has been dropped. At the possible odd
simple node only the value is present. These statements follow from
the full matrix identity and the physical confluent polynomial,
not an inference from coincident eigenvalues. Although
\(|\alpha_j|\le N^2/8\), this alone does not bound a complete word
in an arbitrary recoupling frame.

## 3. An explicit faithful cyclic space for the Newton comparison

Let
\[
 W_d=\operatorname{span}\{|j,d-j\rangle:0\le j\le d\},
 \qquad A=\Omega|_{W_d},\qquad b_0=|0,d\rangle.
\]
This is the physical middle-degree space. Its dimension is \(N\).
The Casimir is the actual tridiagonal matrix, with adjacent entries
\(-(1-Q^j)^2\), \(1\le j\le d\), where \(Q=q^2\).
The pair-algebra proof shows that its minimal polynomial is the full
\(P_N\). In particular \(b_0\) is cyclic.

Put \(S_r=\prod_{a=1}^r2\sin(\pi a/N)\), with \(S_0=1\).
Let \(e_r(z)=S_r^{-2}\prod_{a=0}^{r-1}(c_a-z)\) be the normalized
Newton basis. Define
\[
 U_N:\mathcal A_N\longrightarrow W_d,\qquad
 U_N f=f(A)b_0.
 \tag{10}
\]
This is an explicitly specified matrix: its column \(r\) is
\(e_r(A)b_0\). That column has no coordinates beyond \(r\); its
coordinate at \(r\) is
\[
 \frac{F_r^2}{S_r^2}=(-1)^r q^{r(r+1)}\ne0,
 \qquad F_r=(Q;Q)_r.
 \tag{11}
\]
Indeed only the degree-\(r\) term can reach that coordinate. Its
leading coefficient is \((-1)^r/S_r^2\), and the unique outermost
tridiagonal path contributes \((-1)^rF_r^2\). This proves (11)
and invertibility of (10), without diagonalizing the Casimir.

The external conserved degree-\(d\) space is
\[
 W_d^{\rm ext}=\operatorname{span}\{e_j\otimes e_{d-j}:0\le j\le d\}.
\]
It maps to \(W_d\) under \(T_N\otimes T_N\). Set
\[
 L_N=(T_N\otimes T_N)^{-1}U_N:
                  \mathcal A_N\longrightarrow W_d^{\rm ext}.
 \tag{12}
\]
For every polynomial \(f\),
\[
 L_N^{-1} f(\Omega_{\rm ext})|_{W_d^{\rm ext}} L_N=m_f,
 \qquad
 L_N^{-1} R^{\rm ext}_\pm|_{W_d^{\rm ext}} L_N=M^{\mp1},
 \tag{13}
\]
where \(m_f\) is multiplication by \(f\) on the full quotient and
\(M\) is our specified positive Newton crossing matrix. The first
identity follows immediately from \(U_N(fg)=f(A)U_Ng\); the second
uses (8). All integer crossing powers follow.

The restriction in (13) is faithful on the pair commutant, because
its elements are \(f(\Omega_{\rm ext})\), and the minimal polynomial
on this slice is \(P_N\). No arbitrary physical matrix is being
reconstructed from its middle-degree restriction. Likewise (10)
represents the quotient polynomial; it does not reconstruct an
unreduced higher-degree free-boundary polynomial from residue data.
The diagonal moduli in (11) do not establish a bound on the condition
number of \(U_N\).

## 4. Both adjacent generators on the complete multiplicity module

For overlapping crossings the correct space is the complete
\(N\)-dimensional Hom space from
[the complete source multiplicity construction](actual_complete_source_multiplicity_module.md),
not an independently projected pair at each step. Its explicit map
\(w\mapsto I_w\) identifies \(W_d\) with
\(\operatorname{Hom}_{\rm Hopf,H}(V,V^{\otimes3})\).
Transport that whole construction by defining
\[
 I^{\rm ext}_w=T_N^{-\otimes3} I_w T_N.
 \tag{14}
\]
This is an isomorphism onto the complete Hom space for the transported
Hopf action. The embedded physical space has dimension \(N^2\),
exactly as in the cited construction; (14) does not reduce it to one
copy of \(V\). All intermediate pair Jordan channels remain.

In the original multiplicity coordinates the two physical positive
generators are \(\kappa r_N(A)\) and \(\kappa r_N(B)\), with
\(B=J^{-1}AJ\) and the explicit complete recoupling matrix \(J\)
from that construction. Equation (3) consequently makes the external
positive generators on (14) their literal inverses, simultaneously.
The same argument applies to the complete higher-width invariant
spaces in that note. It does not assert that adjacent Casimirs commute.

Transporting the specified physical cups, caps and marked observation
is necessary to complete a tangle comparison. The local adapter (2),
the cyclic map (12), and the complete multiplicity transport (14)
provide exact coordinates for that task. They supply no noncancellation
or geometric coefficient estimate for arbitrary short fillings.
