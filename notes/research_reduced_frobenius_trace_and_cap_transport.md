# The reduced Frobenius trace and exact transport of the finite caps

Private written proof, 18 November 2026.

The actual reduced braid word has an untruncated polynomial
lift whose root carries can never return in a closed trace.
Its graded trace is the original finite reduced trace divided
by an explicit classical determinant. At the complete color
that determinant is the braid width \(m\). Its meridian
derivative is retained, and its contribution to the original
first-jet closing row cancels by the actual residue equation,
separately in each Casimir pair.

This moves the physical capacity constraints into a specified
closing quotient and then a rational graded-trace prescription.
It does not replace that prescription by a convergent unweighted
Gaussian trace or identify it with a geometric cycle. The original
Verma/Alexander mechanism is already proved in V; the additional
calculation here is its reduced-star and first-jet source adapter.
The complete directs are V, W, R, H and C, pinned below.

## 1. The polynomial lift and its lattice

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
and \(x=-M/q\). The quantum parameter remains fixed while
\(M\) varies near one. Let \(\beta\) be a braid on \(m\ge2\)
heads with one-component closure and writhe \(w_\beta\).
Put \(r=m-1\), \(k=x^N\).

On the physical head \(0\le a<N\), let \(w_a\) be the
original balanced basis and put
\(G_Fw_a=f_aw_a\), where \(f_a=(Q;Q)_a\ne0\).
The normalized basis vector \(f_aw_a\) is identified with
the monomial \(z^a\); operators in this basis are
\(G_F^{-1}AG_F\).
On the infinite space \(\mathbb C[z]\), however, \(z^a\)
is defined independently. It is V's unbalanced Verma
polynomial basis. There is no globally invertible
diagonal matrix with entries \(f_a\): these vanish
when \(a\ge N\).

The identification of root blocks is
\[
 z^{NA+\bar a}\longleftrightarrow z^{\bar a}Y^A,
 \qquad 0\le\bar a<N,\qquad Y=z^N.
 \tag{1}
\]
If the residue factor is written in the original balanced
head basis, only the nonzero normalization \(f_{\bar a}\)
is used. No factorial of the full index is inverted.

For the physical crossings use V's full polynomial Verma
entries, with the original common scalar \(\kappa\):
\[
 \begin{split}
 \widetilde R^+_{b+n,a-n;\,a,b}
 &=\kappa\,x^{-a-b+n}Q^{(a-n)b}
       {a\brack n}_Q(x^{-2}Q^{a-n};Q)_n,\\
 \widetilde R^-_{b-n,a+n;\,a,b}
 &=\kappa^{-1}x^{a+b-n}Q^{-ab}
       {b\brack n}_Q(x^2Q^{1-b};Q)_n .
 \end{split}
 \tag{2}
\]
The respective ranges are \(0\le n\le a\) and \(0\le n\le b\).
The divided factorials have already been cancelled.
Terms \(n\ge N\) are retained; they generally survive
on this lattice and in its meridian derivative.
Every homogeneous total degree is finite dimensional.

For the reduced star use W's word polynomial on every
nonnegative donor input \(a\), without the recipient
projection. Its entry from \((a,b)\) to
\((a-n,b_2+n_2,\ldots,b_r+n_r)\) is the polynomial
\[
 {a\brack a-n,n_2,\ldots,n_r}_Q
       \prod_{j=2}^r x^{-(j-1)n_j}
                        Q^{\,n_j\sum_{2\le i<j}b_i},
 \qquad n=\sum n_j\le a .
 \tag{3}
\]
For its inverse multiply by
\((-1)^nQ^{n(n-1)/2}\). Gaussian multinomials here
are W's inversion-word polynomials, so (3) is defined
at the root even when its displayed factorial quotient
would contain zeros. The diagonal factor is exactly
\[
              \widetilde D z^a
                  =(-1)^aQ^{a(a-1)/2}x^{-2a}z^a .
 \tag{4}
\]
Use the generators
\(\widetilde R_i\) on the remaining heads and
\(\kappa\widetilde S_r\widetilde D\), with their exact
inverses, in the order specified by R. Their product is
\(\widetilde B_\beta(M)\).
All prescribed framing scalars are retained externally
or in the same corresponding finite and lifted words.

These are lifts of the actual reduced generators,
not a new choice of the finite model. For generic
\(q\), the triangular star and its inverse are finite
on each polynomial input and obey
\(F_\Sigma S=S F_1\) by the Gaussian-binomial recursion.
Commutation with the unit raising \(F_1\) makes the
constant-first-column reduction multiplicative.
The same vacuum computation as R gives
\(\kappa S_rD\) for its first generator and the unchanged
physical crossings for the others. On every fixed
total-degree sector these are identities of the
polynomial coefficients in (2)--(4); they specialize
at the root. In particular the signed lifts are
mutually inverse. This justification does not discard
the divided-power terms in (2).

## 2. Frobenius shears for the new star

Here is a direct root calculation of its block action.
For fixed recipient input \(b\), let \(L_j^\pm\)
be W's first-letter operators
\(L_j^\pm=M_{c_j^\pm}T_j^\pm\): apply the indicated
\(Q\)-shifts first, then multiply by the signed \(c_j^\pm\).
The donor letter is relabelled \(1\) here. For \(j>i\),
\[
                     L_j^\pm L_i^\pm=Q L_i^\pm L_j^\pm .
 \tag{5}
\]
The Gaussian-binomial expansion at primitive \(Q\)
therefore gives
\[
       \left(\sum_jL_j^\pm\right)^N
                                  =\sum_j(L_j^\pm)^N .
 \tag{6}
\]
Indeed every mixed degree-\(N\) coefficient has
numerator \(1-Q^N\) and nonzero smaller factorial
denominators; pure powers have coefficient one.
This also proves (6) at even and composite levels.

The positive \(L_j^N\) is multiplication by
\(x^{-N(j-1)}z_j^N\), with \(z_1^N\) for the donor.
For the negative transfer letters its sign is
\[
                 (-1)^NQ^{N(N-1)/2}=-1 .
 \tag{7}
\]
The recipient prefix factor raised to \(N\) is one.
Consequently
\[
 K_{a+N}^{\pm}
   =\left(z_1^N\ \pm\sum_{j=2}^r
                         k^{-(j-1)}z_j^N\right)K_a^\pm .
 \tag{8}
\]
Increasing a recipient input \(b_i\) by \(N\)
instead multiplies its full output by \(z_i^N\).
Thus the star's action on the Frobenius variables is
\[
 S_{\rm Fr}^{\pm}:\quad
 Y_1\longmapsto Y_1\pm\sum_{j=2}^r k^{-(j-1)}Y_j,
 \qquad Y_i\longmapsto Y_i\quad(i\ge2).
 \tag{9}
\]
Iterating (8) proves the complete block statement,
not only the degree-\(N\) row.

More explicitly write input indices as
\(a=NA+\bar a\), \(b_i=NB_i+\bar b_i\).
In a nonzero star term the residue transfers satisfy
\(\sum_i t_i\le\bar a\). Its donor residue is
\(\bar a-\sum t_i\). A recipient carry occurs only
when \(\bar b_i+t_i\ge N\), and decreases the sum of
all residues by \(N\). Without such carries the
coefficient is the physical finite star coefficient
times the ordinary multinomial coefficient of (9).
For the inverse the block-transfer sign is
\((-1)^{\sum C_i}\): dividing its full sign/chirp
by the residue sign/chirp gives precisely that sign.
This is also immediate from (7)--(8).

The diagonal (4) has block factor
\[
                 D_{\rm Fr}:Y_1\longmapsto-k^{-2}Y_1 ,
 \tag{10}
\]
since its coefficient at \(NA+\bar a\), divided by
the coefficient at \(\bar a\), is
\((-k^{-2})^A\). All its residue and half phases remain.

V proves the analogous carry statement for (2):
residue degree never increases, a carry decreases it
by \(N\), and its carry-free block matrices are
\[
 L_+(k)=\begin{pmatrix}1-k^{-2}&k^{-1}\\k^{-1}&0\end{pmatrix},
 \qquad
 L_-(k)=\begin{pmatrix}0&k\\k&1-k^2\end{pmatrix}.
 \tag{11}
\]
The corresponding residue operator is exactly the
physical crossing in the normalized finite basis.
The common \(\kappa^{\pm1}\) belongs to that finite
factor, not to (11).

## 3. Moving the internal caps

Let
\[
 \mathcal P_r=\mathbb C[z_1,\ldots,z_r],\qquad
 \mathcal I_N=(z_1^N,\ldots,z_r^N),\qquad
 P_N:\mathcal P_r\longrightarrow
              \operatorname{span}\{z^a:0\le a_j<N\}
 \tag{12}
\]
be the literal coefficient projection. Every lifted
generator preserves \(\mathcal I_N\). For the star this
follows from (8)--(9); for the physical crossings it
follows from V's carry filtration; (4) is diagonal.
The induced quotient generators are exactly R's
finite all-\(G_F\) generators.

Hence, for every polynomial input,
\[
 P_N\widetilde A_LP_N\cdots P_N\widetilde A_1P_N
              =P_N(\widetilde A_L\cdots\widetilde A_1)P_N .
 \tag{13}
\]
To prove it, write \(f=P_Nf+i\), \(i\in\mathcal I_N\).
Ideal preservation gives
\(P_N\widetilde A f=P_N\widetilde A P_Nf\);
iterate this equality. Thus all sectors which leave
the physical box and return cancel exactly after
the local coefficients are assembled. The equality
is before absolute values. It is not a claim that
individual word-expansion terms outside the box vanish.

The lifts preserve total degree. On a physical input
their total degree is at most \(rd\), so (13) can be
performed wholly inside the finite polynomial space
of degree at most \(rd\). It needs no interchange of
an unbounded Gaussian integral. It holds throughout
the fixed-root meridian germ and after differentiation,
since both the ideal and \(P_N\) are independent of \(M\).
Any original boundary functional on the quotient is
retained at the closing projection. No assertion of
such a transport on a moving-\(q\) germ is made.

There is also a stronger trace statement. Write each
multi-index as \(a=NA+\bar a\), and filter by the
total residue degree \(|\bar a|\). Every local lift
is nonincreasing in this degree. A path contributing
to a diagonal matrix coefficient must return to its
initial residue degree, so it has no carry anywhere.
On the associated graded the whole word is therefore
\[
              B_\beta(M)\ \otimes\
                    \operatorname{Sym}\Gamma_\beta(k),
 \tag{14}
\]
where \(B_\beta\) is the actual normalized finite
reduced word. This is an equality of the trace
contributions, not a splitting of every off-diagonal
matrix entry.

## 4. The exact classical determinant and its unit

The matrix \(\Gamma_\beta\) in (14) has the original
reduced generator order:
physical generators use (11), and the first generator
uses \(S_{\rm Fr}^+D_{\rm Fr}\). It is the quotient
of V's \(m\)-dimensional Burau matrix \(L_\beta(k)\)
by its fixed linear form.

To verify the quotient, on \(m\) variables put
\[
 P_mY_1=Y_1+\sum_{j=2}^m k^{-(j-1)}Y_j,\qquad
 P_mY_i=Y_i\quad(i\ge2).
 \tag{15}
\]
The displayed first image is fixed by every \(L_i\).
Thus \(P_m^{-1}L_\beta P_m\) fixes \(Y_1\).
For \(i\ge2\) its quotient on \(Y_1=0\) is the
unchanged adjacent matrix (11). For \(i=1\),
\[
 Y_2\longmapsto
       -k^{-2}\left(Y_2+\sum_{j=3}^m k^{-(j-2)}Y_j\right)
                    \pmod {Y_1},
 \tag{16}
\]
and the other tail variables are fixed. This is
exactly \(S_{\rm Fr}^+D_{\rm Fr}\), in that order.
The negative generators are its inverse.

Write
\[
 d_\beta(k;\zeta)=\det(I-\zeta\Gamma_\beta(k)),\qquad
 d_\beta(k)=d_\beta(k;1).
 \tag{17}
\]
V's fixed vector is
\(v=(1,k^{-1},\ldots,k^{1-m})^t\). If \(D_\beta(k)\)
is the deleted \(I-L_\beta\) cofactor, V proves
\(\operatorname{adj}(I-L_\beta)=D_\beta vv^t\).
The coefficient of \(t\) in
\(\det(I-L_\beta+tI)\) is both
\(d_\beta(k)\) and the trace of this adjugate.
Together with V's exact Alexander unit, this gives
\[
 \boxed{\quad
 d_\beta(k)=
 k^{\,m-1-w_\beta}\Delta_K(k^2)
                    \sum_{j=0}^{m-1}k^{-2j}.
 \quad}
 \tag{18}
\]
The sum is written explicitly to avoid confusing it
with a symmetrically normalized quantum integer.
The cofactor argument is first over \(\mathbb C(k)\);
the polynomial identity extends through its exceptional
values. It retains every sign and writhe unit.

At \(M=1\), \(k_0=(-q^{-1})^N=(-1)^{N+1}\).
A knot braid has \(m-1-w_\beta\) even, and
\(\Delta_K(1)=1\). Therefore
\[
                            d_\beta(k_0)=m .
 \tag{19}
\]
Equivalently \(L_\beta(k_0)\) is, after a diagonal sign
gauge, the one-cycle strand permutation. Its quotient
has the nontrivial \(m\)-th roots of unity as eigenvalues.
This also checks that no extra scalar is being assigned
to the closing projection.

## 5. Exact graded traces with the actual Cartan marks

On the physical remaining heads put
\[
 K_0=x_0^rQ^{-J},\quad x_0=-q^{-1},\quad
 J=\sum J_j,\quad \varepsilon=(-1)^{(N+1)r}.
 \tag{20}
\]
The same formula on the polynomial lift depends only
on the residue multi-index. Let \(f(K_0)\) be any fixed
function of its \(N\) eigenvalues; in particular use
\(K_0^{\pm1}\) or \(P_{\mathfrak o}K_0^{\pm1}\).
Define the finite polynomial and the formal graded trace
\[
 \begin{split}
 t_f(M;\tau)&=\operatorname{Tr}_{\rm box}
                 \big(\tau^J f(K_0)B_\beta(M)\big),\\
 \widetilde t_f(M;\tau)&=
   \sum_{a\in\mathbb Z_{\ge0}^r}
       \tau^{|a|}f(x_0^rQ^{-|a|})
                         (\widetilde B_\beta(M))_{aa}.
 \end{split}
 \tag{21}
\]
Every coefficient of the second sum is finite.
The no-return trace statement (14) gives exactly
\[
 \boxed{\qquad
 \widetilde t_f(M;\tau)=
       \frac{t_f(M;\tau)}
               {d_\beta(x(M)^N;\tau^N)} .
 \qquad}
 \tag{22}
\]
Indeed the residue contributes \(\tau^{|\bar a|}\)
and the block trace contributes
\(\sum_{A}\tau^{N|A|}
 (\operatorname{Sym}\Gamma_\beta)_{AA}\).
The latter equals \(1/\det(I-\tau^N\Gamma_\beta)\).
One can prove this coefficientwise on diagonal
matrices by geometric series; polynomial identity
then proves it for all matrices, including Jordan blocks.
This is the same elementary trace identity used in V.

Equation (22) is initially a formal power-series identity,
and defines its exact rational continuation in \(\tau\).
At \(\tau=1\) its denominator is nonzero for \(M\)
sufficiently close to one by (19). This is the meaning
of \(\widetilde t_f(M;1)\) below; no convergence of the
unweighted infinite trace has been assumed.

There is an Abel description at \(M=1\) as well.
By (19), the zeros in \(\tau\) of the denominator at
that point lie on the unit circle and none is at one.
The rational function and each fixed meridian derivative
therefore have their Taylor series converging for
\(|\tau|<1\), and their limits as real \(\tau\uparrow1\)
are the stated rational values. Differentiation can
first be done on any smaller closed disk in \(\tau\),
where a common meridian neighborhood is available.
This does not assert convergence at \(\tau=1\)
before continuation.

## 6. The first jet and cancellation of the determinant derivative

Use the original pair projector \(P_{\mathfrak o}\)
of C, or sum over all pairs. Set
\[
 t_{\mathfrak o,\pm}(M)=
       t_{P_{\mathfrak o}K_0^{\pm1}}(M;1),\qquad
 \widetilde t_{\mathfrak o,\pm}(M)=
       \widetilde t_{P_{\mathfrak o}K_0^{\pm1}}(M;1).
 \tag{23}
\]
These are actual finite marked traces or their
specified rational graded continuations. The projectors
in the reduced formula are constant in the occupation
basis, as C proves; the corresponding original total
Casimir projector is its full analytic family.

Put \(d(M)=d_\beta(x(M)^N)\). Equation (22) gives
\[
 t_{\mathfrak o,\pm}=d\,\widetilde t_{\mathfrak o,\pm},\qquad
 t_{\mathfrak o,\pm}'=
       d'\widetilde t_{\mathfrak o,\pm}
                    +d\,\widetilde t_{\mathfrak o,\pm}' .
 \tag{24}
\]
In particular \(d'(1)\) includes
\(Nk_0\,\partial_kd_\beta(k_0)\). The divided powers,
the whole meridian dependence of the word, and this
potentially \(N\)-sized derivative have not been dropped.

C's pairwise residue identity is
\[
        t_{\mathfrak o,+}(1)-t_{\mathfrak o,-}(1)=0 .
 \tag{25}
\]
Since \(d(1)=m\ne0\), it holds for the tilded traces too.
H's original first-jet functional is therefore exactly
\[
 \begin{split}
 \Phi_{\mathfrak o}(W(1))
  &=\frac{t_{\mathfrak o,+}(1)+t_{\mathfrak o,-}(1)}
                         {2\varepsilon}
    +\frac{t_{\mathfrak o,+}'(1)-t_{\mathfrak o,-}'(1)}
                         {2\varepsilon m}\\
  &=m\left[
       \frac{\widetilde t_{\mathfrak o,+}(1)
                         +\widetilde t_{\mathfrak o,-}(1)}
                         {2\varepsilon}
       +\frac{\widetilde t_{\mathfrak o,+}'(1)
                         -\widetilde t_{\mathfrak o,-}'(1)}
                         {2\varepsilon m}\right].
 \end{split}
 \tag{26}
\]
The extra term in (24) is precisely
\(d'(1)(\widetilde t_{\mathfrak o,+}
-\widetilde t_{\mathfrak o,-})/(2\varepsilon m)\);
it vanishes by (25). Thus its cancellation is an
original-source identity, not a constant-determinant
approximation. Summing (26) gives the whole source.
All external scalar framing and normalization lines
multiply both sides unchanged.

The cancellation in (26) is a statement about the whole
finite source and C's actual Casimir-pair projectors.
It has not been proved for an individual off-circle
geometric saddle or a separately chosen relative chain.
On such a component the residue numerator need not vanish;
the term involving \(d'(1)\), which can have size \(O(N)\),
must remain until a source-compatible residue pairing is
established. Consequently a marked action derivative of a
finite reduced sector cannot be transferred unchanged to a
bare Verma sector by deleting that term.

The full meridian form is also retained. On the punctured
disk the same factorization gives
\[
 \Phi_{\mathfrak o}(M)=d(M)\,
 \frac{D_N(M)}
          {\varepsilon(M^{mN}-M^{-mN})}
 \left(M^m\widetilde t_{\mathfrak o,+}(M)
                     -M^{-m}\widetilde t_{\mathfrak o,-}(M)\right),
 \tag{27}
\]
where \(D_N(M)=(M^N-M^{-N})/(M-M^{-1})\).
Its removable value is exactly (26).
This retains the full peripheral determinant (18);
only its proved complete value is \(m\).

## 7. What has been transported

Equations (13), (22) and (26) give an exact global
assembly of the finite cap data for every fixed
actual braid word in the stated source convention.
Internal capacity exits cannot return in the assembled
trace. The remaining Frobenius block sum is a specified
rational period with an explicit determinant, and
its determinant derivative cancels in the first-jet
closing row, including each Casimir pair.

This applies to a fixed knot obtained after any
specified finite filling once its actual braid and
normalization are retained. It is not a uniform
asymptotic estimate in the filling parameters.
For an external coupon not expressed by these
generators, ideal preservation suffices for (13),
but its own associated-graded factor must be supplied
before claiming the scalar determinant formula (22).
An arbitrary short exterior operator is not declared
scalar on a Casimir multiplicity space.

The graded continuation has not been identified with
a geometric thimble, nor has any actual nonzero
coefficient or lower bound been proved. The untruncated
polynomial kernels still have their own phases, poles
under continuation and closing prescription. No
termwise removal of an entire-function cap from a
divergent Gaussian integral is authorized by (13).
Moving-\(q\) normals and ordinary-color closed jets
require their original extra adapters.

## Complete proof-source pins

* V: notes/frobenius_verma_period.md,
  SHA256 b11489368e7ac1106c7a5e760154b0713dfbc7eaf9b76193438df57b48041a90.
* W: notes/research_reduced_euler_star_complex_word_kernel.md,
  SHA256 6baac1f8303d21be4a5c3f6c809795272dd51d3e0060e13843e0f25958902fdb.
* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* H: notes/research_scalar_prefix_kernel_and_first_meridian_jet.md,
  SHA256 d7d82848a1b3f50709352905bafcc7ddfee36f41e434bf5de4663b4b6181dc9e.
* C: notes/research_reduced_casimir_pair_localizer.md,
  SHA256 e5307ed7e424ba181db9b73f8473342a094ed85caf0b521b4aa965bb78e3c4ea.

All five complete directs were read nontruncated in the active
author sequence, with unchanged complete reads retained where
specified in the review record. Every used implication was
checked. Only written mathematics and text/hash operations
were used; frozen and public files were not edited.
