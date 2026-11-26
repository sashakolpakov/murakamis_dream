# The exact Fourier pairing at the adjacent three-crossing boundary

This audit retains the actual boundary polynomial of the adjacent
three-crossing pendant. Existing Fourier identities preserve that
source, but do not identify it with a positive norm. There is an
elementary all-level obstruction to a common-phase positive pairing
in its original color coordinates. This does not exclude a new
coherent transformation or a source-specific lower estimate.

## 1. The original pairing and its Fourier transform

Use the original Newton matrices and notation of
[the boundary-current theorem](research_three_crossing_boundary_current.md):
\(q=e^{\pi i/N}\), \(Q=q^2\), \(D=N-1\),
\(\kappa=e^{\pi iD^2/(2N)}\), and \(J\) is index reversal.
Set
\[
 P=M^3,\qquad \alpha=P e_0,\qquad
 f=JPJP e_0=P^{\mathsf T}\alpha,
 \qquad \mathbf e(w)=(e_0(w),\ldots,e_D(w))^{\mathsf T}.
 \tag{1}
\]
Here \(JPJ=P^{\mathsf T}\) is the exact original turn identity.
In particular the entire free-boundary source is
\[
 F_N(w)=\mathbf e(w)^{\mathsf T}f
       =b(w)^{\mathsf T}\alpha,
       \qquad b(w)=P\mathbf e(w).
 \tag{2}
\]
All terms in (1)--(2) are full degree-less-than-\(N\) quotient
vectors, so these identities retain both physical values and the
first normals at double roots. Evaluation at \(w=-2\) does not
replace the quotient by its reduced algebra.

Write \(\mathsf D_{jj}=q^{j(j+2)}\) and
\(\beta=\kappa^{-3}\mathsf D^{-1}\alpha\). For the unitary Fourier
transform
\[
 \widehat v(m)=N^{-1/2}\sum_{j=0}^{N-1}v_jQ^{-mj},
\]
finite character orthogonality gives the exact formula
\[
 F_N(w)=\kappa^3\sum_{m=0}^{N-1}
       \widehat\beta(m)\,
       \widehat{\mathsf D b(w)}(-m).
 \tag{3}
\]
The minus sign is taken modulo \(N\). Indeed summing over \(m\)
forces the two original color indices to agree. There is no complex
conjugation in this bilinear Parseval identity.

The [proved Fourier packet](research_three_crossing_fourier_packet.md)
controls the first factor in (3), including its nonzero Gaussian
window. It does not control the phase or observed projection of the
second factor, which includes the next original crossing run.
The positive factorial approximation to \(\beta\) has relative
Euclidean error \(O(N^{-1})\); in (2) its absolute propagated error
is bounded by \(O(N^{-1})\|\alpha\|\,\|b(w)\|\). A lower bound
for the pairing still requires control at the scale of the actual
pairing, not only at the scale of those two norms.

## 2. The first two colors exclude the direct positive pairing

Put \(\theta=\pi/N\) and
\[
 r=2\cos(2\theta)-1,\qquad
 e=e_1(-2)=\frac1{4\sin^2(\theta/2)}.
 \tag{4}
\]
The last equality follows directly from
\(e_1(w)=(c_0-w)/(4\sin^2\theta)\),
\(c_0=2\cos\theta\). The upper-left two-by-two block of the
original lower-triangular crossing is
\[
 \kappa^{-1}M\big|_{\{0,1\}}=
 \begin{pmatrix}1&0\\-q&-q^2\end{pmatrix}.
\]
Cubing it gives
\[
 \kappa^{-3}P\big|_{\{0,1\}}=
 \begin{pmatrix}1&0\\-q^3r&-q^6\end{pmatrix}.
 \tag{5}
\]
Consequently the first two summands of (2), after removal of the
original common scalar \(\kappa^6\), are exactly
\[
 \kappa^{-6}\alpha_0b_0(-2)=1,
 \qquad
 \kappa^{-6}\alpha_1b_1(-2)=q^6r^2+q^9re.
 \tag{6}
\]
For every \(N\ge10\), \(r,e>0\),
\(\sin(6\theta)>0\), and \(\sin(9\theta)>0\). Thus
\[
 \operatorname{Im}\bigl(\kappa^{-6}\alpha_1b_1(-2)\bigr)
       =r^2\sin(6\theta)+re\sin(9\theta)>0.
 \tag{7}
\]
There is therefore no unit scalar \(\lambda\) and no collection
of nonnegative real numbers \(d_j\) for which
\[
       b_j(-2)=\lambda d_j\overline{\alpha_j}
       \quad\hbox{for every }j.
 \tag{8}
\]
The zeroth coordinate would force \(d_0=1\) and
\(\lambda=\kappa^6\); the first coordinate then contradicts (7).
This rules out the direct positive diagonal pairing even if its
weights are allowed to depend on this source and on \(N\).
The negative pendant is the complex conjugate and has the same
obstruction. No numerical pattern is used in this proof.

In particular \(\overline{b(-2)}\) and \(\alpha\) are not parallel.
Applying the same unitary change of basis to the two vectors in
\(F_N(-2)=\langle\overline{b(-2)},\alpha\rangle\) preserves this
fact. Thus a Fourier change of basis alone cannot identify those
two specified vectors and turn this pairing into their squared norm.

This statement does not assert that the complete sum cannot have
a useful explicit phase. It excludes termwise phase coherence and
the specific positive-diagonal Gram representation (8). It also
does not exclude a non-diagonal transform with a separately proved
source estimate.

## 3. What the earlier positive and polarized identities supply

The relevant prior results have distinct scopes.

* [Whole two-cut Fourier polarization](actual_two_cut_fourier_polarization_and_cap.md)
  and [the one-index Ward reduction](actual_one_index_fourier_source_and_ward_reduction.md)
  preserve the actual source and its endpoint carries. Their
  remaining Fourier-label contraction is complex. The
  [polarized geometric normal block](actual_fourier_polarized_geometric_normal_block.md)
  is a nonzero local formal block, with global survival explicitly
  left open.
* [The Fourier--Hermite filling Gram](actual_filling_fourier_hermite_gram.md)
  is full rank and polynomially conditioned, but the actual
  filling is the single pairing \(y_\ell^{\mathsf T}z\).
  Its exact dual norm supplies a Cauchy upper bound. Its own
  source-exact normalization example has exponentially large
  positive packet energy and a selected filled scalar of modulus
  one. Thus conditioning of the whole Gram is not a lower bound
  for a specified filling observation.
* [The weighted plat Fourier identity](actual_weighted_fourier_plat_energy.md)
  retains a compulsory positive dual metric and the original
  marked cap. Its proved comparison is an upper bound and retains
  a coherent sewing probability. It does not replace the two
  factors in (3) by conjugates.
* [The complete-meridian ordinary-color remainder bound](ordinary_color_plancherel_bound_audit.md)
  applies to the stated closed one-component knot and its marked
  root-orbit color family. The present Conway boundary evaluation
  has not been identified with that family; no polynomial
  ordinary-color remainder for (2) follows from that theorem.

Thus the nonzero Fourier window of the first run is an input to
the next crossing problem, while the positive identities above do
not remove the actual boundary observation. The
[full local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
now proves that observation by an exact contour identity and
strict estimates for every complementary term. It includes the
nonzero selected coefficient and the original normals. Its proof
does not identify the bilinear pairing with a positive norm.
