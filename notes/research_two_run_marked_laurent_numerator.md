# The marked Laurent numerator of an original two-run knot

Research note, 3 November 2026.

For every literal two-run knot, the original scalar is determined by
a unique finite Laurent-coefficient system with bandwidth independent
of the quantum level. Its forcing uses the fixed classical denominator
of the resonant source monodromy. The numerator retains the original
reset vector, the turn pairing, and the entire coherent color sum.
The closing scalar is an evaluation of that numerator, without a
remaining derivative.

This is an exact structural theorem. It does not estimate that
evaluation, prove a nonzero asymptotic coefficient, or replace a
geometric contour theorem.

## 1. The original matrices and the fixed denominator

Fix nonzero signed integers \(a,b\), with at least one even. These
are precisely the one-component cases for the original cylindrical
closure \(C(R^bT(R^a))\), by the literal three-pairing calculation in
Section 6 of the
[source-jet note](research_two_run_monodromy_source_jets.md).
No hyperbolicity assumption is needed for the identities below.

At level \(N\ge2\), put
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad D=N-1,\quad
 \kappa=\exp\!\left(\frac{\pi iD^2}{2N}\right),\qquad
 k=\lceil|a|/2\rceil,\quad \ell=\lceil|b|/2\rceil,\quad m=k\ell.
 \tag{1}
\]
Let \(\sigma_p=\operatorname{sgn}p\) and let \(e_p\) be one for
even \(|p|\), zero for odd \(|p|\). Set \(s=e_a+e_b\in\{1,2\}\).
Use the polynomial original run transfer
\(\mathcal T_p(0;z)\) from equation (4) of the source-jet note.
The natural signed one-clock transfer and its marked output row are
\[
 A(x)=\mathcal T_a(0;x^{\sigma_a})
                  \otimes\mathcal T_b(0;x^{\sigma_b}),\qquad
 c^T=\mathbf e_k^T\otimes\mathbf e_\ell^T .
 \tag{2}
\]
The original reset vector is
\[
 w_0=v_a\otimes v_b,\qquad
 (v_p)_j=(q^{\sigma_p})^{k_p-j},\qquad c^Tw_0=1.
 \tag{3}
\]
In particular it is not an arbitrary eigenvector normalization.

Define the augmented color transfer and the full product by
\[
 F(x)=\begin{pmatrix}A(x)&0\\c^TA(x)&1\end{pmatrix},\qquad
 \mathcal M_N(x)=F(Q^{N-1}x)\cdots F(x)
       =\begin{pmatrix}U_N(x)&0\\r_N(x)&1\end{pmatrix}.
 \tag{4}
\]
The reset factor \(F(x)\) is retained. The original source is
\[
 \mathcal Z_{a,b,N}
   =\phi_N(R^bT(R^a))
   =\mathbf e_D^TM^bJM^a\mathbf e_0
   =\kappa^{a+b}\zeta_D,
 \tag{5}
\]
where \(\zeta_D\) is the accumulator initialized with one, as in
the [exact two-run transfer](research_two_run_source_transfer.md).
Thus (4) uses the original complete Newton quotient and its normals,
not a semisimple replacement.

Let \(T^{\mathrm{cl}}_r(X)\) be the same run transfer with \(q=1\)
and positive power \(r\). Define a fixed Laurent polynomial
\[
 \mathcal D_{a,b}(X)=
 \det\!\left[
 I_m-T^{\mathrm{cl}}_{|a|}(X^{\sigma_a})
                 \otimes T^{\mathrm{cl}}_{|b|}(X^{\sigma_b})
 \right].
 \tag{6}
\]
The independently proved
[resonant characteristic theorem](research_resonant_source_monodromy_characteristic.md)
gives the exact identity
\[
        \det(I_m-U_N(x))=\mathcal D_{a,b}(x^N).
 \tag{7}
\]
The two level-parity signs cancel in the tensor product.
In the present knot cases \(U_N(1)=0\), so
\(\mathcal D_{a,b}(1)=1\). In particular (6) is not the zero
polynomial.

## 2. A finite Laurent numerator and its exact equation

Put
\[
 L=-\!\!\sum_{\substack{p\in(a,b)\\p<0}}\!(|p|-1),\qquad
 R=\!\!\sum_{\substack{p\in(a,b)\\p>0}}\!(|p|-1).
 \tag{8}
\]
Thus \(L\le0\le R\); repeated powers in the ordered pair are
counted twice.

**Lemma 1.** A single original transfer
\(\mathcal T_p(0;z)\) is a polynomial of degree at most
\(|p|-1\), and its constant term is \(-q^{\sigma_p}I_{k_p}\).
Consequently
\[
                  A(x)=\sum_{t=L}^{R}\mathsf A_t x^t.
 \tag{9}
\]

*Proof.* In the explicit polynomial formula for
\(\mathcal B_k(q_pz;q_p)\), entry \((i,j)\) starts at degree
\(|i-j|+1\) and has degree at most \(2k-i-j+1\).
For an even transfer the factor \(1-z^{-1}\) creates no negative
degree. The largest degree is \(2k-1=|p|-1\), and the constant
term comes only from the diagonal leading term \(q_pz\).
For an odd transfer, its first column is multiplied by
\(-z^{-1}\); other columns by \(1-z^{-1}\). The first-column
degree is at most \(2k-i-1\), and the other-column degree at most
\(2k-i-j+1\), both at most \(2k-2=|p|-1\).
The same diagonal computation gives the constant term.
This includes \(k=1,p=\pm1\). Substitution of \(x^{\sigma_p}\)
and tensor multiplication prove (9). \(\square\)

Define the marked row
\[
 \boxed{\quad
 P_N(x)=r_N(x)\operatorname{adj}(I_m-U_N(x)).
 \quad}                                                        \tag{10}
\]
Equivalently, where the inverse exists,
\(P_N=\mathfrak h_N\mathcal D_{a,b}(x^N)\), with
\(\mathfrak h_N=r_N(I_m-U_N)^{-1}\).

**Theorem 2.** The row \(P_N\) is the unique Laurent-polynomial
solution of
\[
 \boxed{\quad
 P_N(Qx)A(x)=P_N(x)-\mathcal D_{a,b}(x^N)c^TA(x).
 \quad}                                                        \tag{11}
\]
It has the explicit support bound
\[
               P_N(x)=\sum_{j=mNL}^{mNR}P_{N,j}x^j.
 \tag{12}
\]
Uniqueness also holds among rational rows.

*Proof.* Every factor of (4) has Laurent support in \([L,R]\),
since that interval includes zero. Thus \(U_N,r_N\) have support
in \([NL,NR]\). Every cofactor of \(I_m-U_N\) has support in
\([(m-1)NL,(m-1)NR]\). This proves (12).

Exact cyclic transport, including the reset, gives
\[
 U_N(Qx)A(x)=A(x)U_N(x),\qquad
 r_N(Qx)A(x)=r_N(x)+c^TA(x)(U_N(x)-I).
 \tag{13}
\]
On the nonempty open set where the inverses exist, these equations
imply
\(\mathfrak h_N(Qx)A(x)=\mathfrak h_N(x)-c^TA(x)\).
Since \((Qx)^N=x^N\), multiplication by (7) proves (11) on
that open set and then as a Laurent-polynomial identity.
No inverse is required at a reset point in (11).

If \(V\) is the difference of two rational solutions, then
\(V(Qx)A(x)=V(x)\). Iterating through the \(N\) colors gives
\(V(x)U_N(x)=V(x)\). Equation (7), which is nonzero, implies
\(V=0\) as a rational row. This proves uniqueness without
additional boundedness or positivity assumptions. \(\square\)

The theorem does not say that the characteristic polynomial alone
determines the source. It also uses the complete ordered matrix
\(A(x)\), the original marked row \(c^T\), and the inhomogeneous
term in (11).

## 3. The finite Fourier system and the actual scalar

Write
\(\mathcal D_{a,b}(X)=\sum_v d_vX^v\).
Equation (6) and Lemma 1 give the fixed support \(mL\le v\le mR\).
Equating Laurent coefficients in (11) gives
\[
 \boxed{\quad
 P_{N,j}
  -\sum_{t=L}^{R}Q^{j-t}P_{N,j-t}\mathsf A_t
    =\sum_{\substack{mL\le v\le mR,\ L\le t\le R\\Nv+t=j}}
                       d_vc^T\mathsf A_t .
 \quad}                                                        \tag{14}
\]
Set \(P_{N,j}=0\) outside (12), and impose (14) for
\[
                    mNL+L\le j\le mNR+R.
 \tag{15}
\]
All equations outside this range vanish identically.
This is a finite linear system with a unique solution, by
Theorem 2. Its bandwidth is at most \(R-L\), independent of \(N\).
The coefficients containing \(Q^j\) are \(N\)-periodic in \(j\),
and the forcing is confined to the fixed-width intervals
\([Nv+L,Nv+R]\). Overlaps at small \(N\) are included in the sum;
no separation of these intervals is assumed. The coefficients
\(\mathsf A_t\) still contain the exact root-of-unity phases.

The original closing scalar can be recovered by an evaluation:

**Theorem 3.** For every pair in the knot scope of Section 1,
\[
 \boxed{\quad
 \mathcal Z_{a,b,N}
   =\kappa^{a+b}\bigl[\,1+P_N(Q)w_0\,\bigr]
   =\kappa^{a+b}
       \left[\,1+\sum_jQ^jP_{N,j}w_0\,\right].
 \quad}                                                        \tag{16}
\]

*Proof.* Retain the exact reset constants from the source-jet
theorem: \(\chi=c_ac_b\), the nonzero reset row
\(h_0^T=d_a^T\otimes d_b^T\), and
\(\epsilon=\sigma_a^{e_a}\sigma_b^{e_b}\).
The signed-clock reset identities are
\[
 \begin{split}
 A(x)&=\chi\epsilon(x-1)^s w_0h_0^T+O((x-1)^{s+1}),\\
 r_N(x)&=\chi\epsilon(x-1)^s\zeta_Dh_0^T
                                           +O((x-1)^{s+1}).
 \end{split}                                                    \tag{17}
\]
Since \(U_N(1)=0\), formula (10) gives the same leading
coefficient for \(P_N\) as for \(r_N\).
The polynomial \(\mathcal D_{a,b}(x^N)\) equals one at \(x=1\);
it also equals one at \(x=Q\). Taking the coefficient of
\((x-1)^s\) in (11) gives
\[
              P_N(Q)w_0h_0^T=(\zeta_D-c^Tw_0)h_0^T.
 \tag{18}
\]
The reset normalization (3) and \(h_0^T\ne0\) yield
\(P_N(Q)w_0=\zeta_D-1\). Equation (5) proves (16).
\(\square\)

For example, the actual pair \((-4,-5)\) has \(m=6,L=-7,R=0\).
Its uniquely specified row in (14) has six coordinates and
support contained in \([-42N,0]\), with forcing only in
width-seven neighborhoods of the multiples of \(N\) occurring
in the fixed polynomial \(\mathcal D_{-4,-5}\).
Formula (16) computes the original
\(\phi_N(R^{-5}T(R^{-4}))\), including its \(\kappa^{-9}\) unit.
No rational-tangle or endpoint identification is being changed.

For two positive powers, \(\mathsf A_0=QI_m\); for two negative
powers, \(\mathsf A_0=Q^{-1}I_m\). Thus the coefficient of
\(P_{N,j}\) in (14) is respectively \(1-Q^{j+1}\) or
\(1-Q^{j-1}\). These are genuine resonant indices. Dividing by
them and discarding their compatibility equations would change
the unique original solution. For opposite signs the middle
coefficient \(\mathsf A_0\) need not be scalar.

## 4. Reset divisibility and residues away from it

The exact numerator and denominator have the reset divisibilities
\[
 (x-1)^s\mid P_N(x),\qquad
 (x^N-1)^s\mid U_N(x)\ \text{entrywise},\qquad
 (X-1)^s\mid\mathcal D_{a,b}(X)-1.
 \tag{19}
\]
The first follows from the rightmost factor \(A(x)\) in every
term of \(r_N\). The second follows because the even-run zero in
each of the \(N\) color factors is scalar and can be taken out
of the product. The determinant then proves the third; equivalently,
one may use the same reset factors in (6). All divisibilities
are in the relevant Laurent-polynomial ring.

There is also an exact residue transport, without a nonvanishing
assertion. Suppose \(\alpha\ne0\) is a simple zero of
\(\mathcal D_{a,b}\), and let \(x_0^N=\alpha\). The meromorphic
affine row has residue
\[
 \mathcal R(x_0)=
       \frac{P_N(x_0)}
            {N x_0^{N-1}\mathcal D_{a,b}'(\alpha)}.
 \tag{20}
\]
It is allowed to be zero. Taking residues in the multiplied
affine equation gives
\[
 \boxed{\quad
 \mathcal R(Qx_0)A(x_0)=Q\,\mathcal R(x_0),\qquad
 \mathcal R(x_0)U_N(x_0)=\mathcal R(x_0).
 \quad}                                                        \tag{21}
\]
The factor \(Q\) comes from the change of variable in
\(\mathfrak h_N(Qx)\). Since \(\alpha\ne1\), none of these
orbit points is a reset, and all \(A(Q^jx_0)\) are invertible
by the exact transfer determinant formula. Equation (21)
therefore transports the same marked residue around that
classical denominator root. It does not supply its size or
prove that the original forcing excites it.

The forcing gives a precise criterion for that last question.
It is a finite period on the invariant line of the cyclic
transfer, with its original output row retained.

**Proposition 4.** Under the simple-root hypotheses of (20), set
\[
 x_j=Q^jx_0,\qquad A_j=A(x_j),\qquad
 0\ne v_0\in\ker(I-U_N(x_0)),\qquad
 v_{j+1}=A_jv_j\quad(0\le j<N).
 \tag{22}
\]
The kernel is one-dimensional and \(v_N=v_0\). Define its marked
period by
\[
                    \Pi_N(v_0)=\sum_{j=1}^N c^Tv_j .
 \tag{23}
\]
Then the following are equivalent:

1. The affine row has a removable singularity at \(x_0\).
2. Its residue in (20) is zero.
3. \(\Pi_N(v_0)=0\).
4. The finite cyclic equations
   \[
     h_{j+1}A_j=h_j-c^TA_j,\qquad h_N=h_0,
                   \quad 0\le j<N
     \tag{24}
   \]
   have a solution in rows \(h_j\).

If these conditions hold, the solutions of (24) form an affine
line whose direction is the left kernel of \(I-U_N(x_0)\).
If they fail, the affine row has a nonzero simple pole at every
point of this clock orbit. Vanishing of (23) is independent of
the nonzero normalization of \(v_0\).

*Proof.* The determinant in (7) has a simple zero at \(x_0\).
Its derivative is nonzero because \(x_0\ne0\) and
\(\mathcal D_{a,b}'(\alpha)\ne0\). Jacobi's determinant formula
therefore implies that the adjugate of \(I-U_N(x_0)\) is nonzero.
The matrix has corank exactly one. Write its adjugate as
\(\gamma v_0\ell_0\), with \(\gamma\ne0\) and a nonzero row
\(\ell_0\) in its left kernel. This factorization needs no
assumption that the eigenvalue one of \(U_N(x_0)\) is semisimple.

Multiplying the blocks in (4) shows directly that
\[
 r_N(x_0)=\sum_{j=0}^{N-1}c^TA_jA_{j-1}\cdots A_0,
 \qquad r_N(x_0)v_0=\Pi_N(v_0).
 \tag{25}
\]
Thus
\[
                P_N(x_0)=\gamma\Pi_N(v_0)\ell_0.
 \tag{26}
\]
Since the denominator has a simple zero, (20) and (26) prove
the equivalence of the first three conditions. All \(A_j\)
are invertible because \(\alpha\ne1\), and (22) closes since
\(U_N(x_0)v_0=v_0\).

Iterating (24), retaining its order, gives
\[
                h_0(I-U_N(x_0))=r_N(x_0).
 \tag{27}
\]
Conversely, a solution \(h_0\) of (27) determines the other rows
successively by (24); equation (27) gives \(h_N=h_0\).
Because \(I-U_N(x_0)\) has corank one, (27) is solvable exactly
when \(r_N(x_0)v_0=0\). When solvable its set of solutions is
a translate of the one-dimensional left kernel. This proves
the remaining assertions about (24). Finally (21) and the
invertibility of every \(A_j\) propagate a nonzero residue
around the whole orbit. \(\square\)

The affine line in Proposition 4 is a torsor under an additive
one-dimensional vector space: choosing one cyclic solution
identifies every other solution by adding a homogeneous one.
It exists at the resonant orbit only when its period obstruction
vanishes. Away from the determinant zeros the cyclic solution
is unique. Neither this local description nor a root of the
classical denominator forces the marked period to be nonzero.

Theorems 2--3 reduce the original coherent scalar to a unique
forced finite-band coefficient problem. The unresolved analytic
step is an estimate of the marked evaluation in (16), or of
the residues and their connection coefficients. An absolute
bound for the transfers, a denominator eigenvalue, or the
nonzero formal determinant of that coefficient problem does
not alone provide such an estimate.

The [source-jet diagnostic](../experiments/check_two_run_monodromy_source_jets.py)
tests the original matrix normalizations, cyclic and affine
identities, and the classical characteristic denominator at
arbitrary auxiliary clocks. Its
[saved record](../repro/results/research-two-run-monodromy-source-jets.json)
is a finite algebra diagnostic, not an asymptotic certificate.
